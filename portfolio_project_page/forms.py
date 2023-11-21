from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from .models import Page
import zipfile
import os

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'       # ['download_zip_images', ]

    """def clean permet de valider les inputs sur un formulaire quelconque dans notre cas sur le formulaire admin, le programme effectura cette fonction avant de faire une vérification automatique globale des entrées."""
    def clean(self):
        # Id project ne prend pas de valeur None il fera automatiquement un message d'erreur.
        # Vérifier l'integrité des IDs
        try:        # à chaque modif d'un champs ajouter try except Key error avant.
            if int(self.cleaned_data['id_project']) > 0:
                try:
                    # voir si titres existent pour la suite de cette condition
                    titre1_exist = self.cleaned_data['title_1']
                    titre2_exist = self.cleaned_data['title_2']
                except KeyError:
                    raise forms.ValidationError({'title_1': ''})
                try: 
                    id_provide = self.cleaned_data['id_project']
                    page_exist = Page.objects.get(id_project=id_provide)

                    if page_exist.id_project == id_provide:
                        if page_exist.title_1 != titre1_exist and page_exist.title_2 != titre2_exist:
                            # donc ceci est une nouvelle page
                            raise forms.ValidationError({'id_project': f"L'ID correspond déjà un autre projet."})
                except ObjectDoesNotExist:
                    self.cleaned_data['id_project']
                # retourne une erreur si ID = None
            else:
                raise forms.ValidationError({'id_project': f"L'ID doit être supérieur ou égal à 1."})
        except KeyError:
            raise forms.ValidationError({'id_project': ''})
        
        '''try:
            file = self.cleaned_data['download_zip_images']
            file_name_extend = str(file)        # 'file.zip'
            try: 
                filename, ext = file_name_extend.split('.')
            except ValueError:
                # si pas d'extension c'est un dossier, fait return pas besoin de la suite
                return
        except KeyError:
            raise forms.ValidationError({'download_zip_images': ''})        # raise str vide car Django fournit un avrtissement auto lorsque le champs de l'objet est vide.

        # Vérifie si le contenue est un fichier zip et qu'il contient des fichiers images.
        if ext == 'zip':
            with zipfile.ZipFile(file, 'r') as zip_file:
                file_list = zip_file.namelist()
                # créer un fichier d'extraction pour le fichier zip en question
                path = os.path.join(settings.MEDIA_ROOT, 'zip_images', filename)
                # si le fichier existe
                if not os.path.exists(path):
                    os.mkdir(path)
                    for file_l in file_list:
                        file_extend_image = file_l.split('.')
                        if file_extend_image[-1] == 'jpg' or file_extend_image[-1] == 'png':
                            continue
                            # self.extract_zipfile(path, zip_file, file_l)
                        else:
                            raise forms.ValidationError({'download_zip_images': 'LE fichier zip doit contenir uniquement des fichier JPEG ou PNG.'}) 
                # si le fichier existe déjà
                else:
                    raise forms.ValidationError({'download_zip_images': 'Un fichier du même nom est déjà existant'})
        elif ext == 'jpg' or ext == 'png':
            return
        else:
            raise forms.ValidationError({'download_zip_images': 'Uniquement image ou fichier zip sont permisent.'})'''
