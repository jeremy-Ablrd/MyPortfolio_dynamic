from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.contrib import admin
from .models import Page
from .forms import PageForm
from django.conf import settings
import os
import shutil
from PIL import Image




# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ("title_1", "title_2", "id_project", "description")
    exclude = ('slug',)
    actions = ['delete_selected']       # action from the function below
    form = PageForm

    def download_zip_images_change(self, object):
        url = object.download_zip_images.url
        filename = os.path.basename(url)
        folder= filename.split('.')[0]
        object.download_zip_images.name = os.path.join('zip_images', folder)
        object.save()
    
    def extract_zipfile(self, path_folder, zip, image_filename):
        # for read txt file (or short file) : zip_file.read(filename)
        file = zip.open(image_filename, 'r')
        # sauvegarde des fichiers images jpeg et png
        filename = os.path.join(path_folder, image_filename)
        image = Image.open(file)
        if image_filename.split('.')[1] == 'jpg':
            image.save(filename, format='JPEG')
        image.save(filename, format='PNG')
        file.close()

    # -- supprime l'image dans le répertoire lorsque celui-ci est supprimer dans l'interface admin
    def delete_model(self, request, obj):
        # Remove the file from the file system when the image is deleted
        if obj.thumbnail:
            os.remove(os.path.join(settings.MEDIA_ROOT, obj.thumbnail.path))
        if obj.download_zip_images:
            # fichier extrait du zip
            folder_path = os.path.join(settings.MEDIA_ROOT, obj.download_zip_images.path)
            shutil.rmtree(folder_path)
            # fichier zip
            os.remove(folder_path + '.zip') 
        super().delete_model(request, obj)

    # -- permet de faire une suppression multiple sur les pages projets
    def delete_selected(self, request, queryset):
        for objs in queryset:
            if objs.thumbnail:
                image_path = os.path.join(settings.MEDIA_ROOT, objs.thumbnail.path)
                os.remove(image_path)
            # suppression du fichier zip et fichier d'extraction avec le path
            if objs.download_zip_images:
                # -- raise ValidationError(f"{objs.download_zip_images}")
                # pour fichier extraite
                folder_path = os.path.join(settings.MEDIA_ROOT, objs.download_zip_images.name)
                # -- raise ValidationError(f"{folder_path}")
                shutil.rmtree(folder_path)
                # pour fichier zip
                os.remove(folder_path + '.zip')    # shutil.rmtree doesn't work for delete zip file  
        queryset.delete()

    def save_model(self, request, obj, form, change):
        # évite les doublons d'images lorsque celui-ci est télécharger une nouvelle fois dans l'admin
        if change:
            old_obj = self.model.objects.get(pk=obj.pk)
            #
            if old_obj.id_project == obj.id_project:
                obj.id_project = old_obj.id_project
            #
            if old_obj.thumbnail != obj.thumbnail:
                if old_obj.thumbnail:
                    image_path = os.path.join(settings.MEDIA_ROOT, old_obj.thumbnail.name)
                    os.remove(image_path)
            # changer répertoire du fichier zip
            if old_obj.download_zip_images.name != obj.download_zip_images.name:
                if old_obj.download_zip_images.name:
                    folder_path = os.path.join(settings.MEDIA_ROOT, old_obj.download_zip_images.name)
                    shutil.rmtree(folder_path)
                    os.remove(folder_path + '.zip')

        # Dans le cas ou le zip file soit extrait avant la sauvegarde de celui ci
        # try:
        #     stored_id = Page.objects.get(id_project=str(obj.id_project))
        #     if stored_id == obj.id_project:
        #         raise (f"Cette ID correspond déjà à la page: {stored_id}.")
        # except Page.DoesNotExist:
        #     pass

        obj.save()
        self.download_zip_images_change(obj)        # changer le path dans la base de données
        ## -- EXTRACTION DU FICHIER ZIP -- ##
        # path->obj.download.path, with zipfile, for(list des images), recuperer nom image
        # self.extract_zipfile()


    # -- pour donner les permission de suppression.
    def has_delete_permission(self, request, obj=None):
        return True    

admin.site.register(Page, PageAdmin)

