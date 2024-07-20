from django.contrib import admin
from . import models
# Register your models here.
class NotesAdmin(admin.ModelAdmin): 
    list_display = ('title',)

admin.site.register(models.Notes, NotesAdmin)#register that that model is attached to this admin model