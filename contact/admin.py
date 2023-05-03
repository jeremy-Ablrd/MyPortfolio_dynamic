from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("society", "name", "created_at")

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return super().has_change_permission(request, obj)

    # --- remove the delete permission --- #
    # def has_delete_permission(self, request, obj=None):
    #     return False

admin.site.register(Contact, ContactAdmin)
