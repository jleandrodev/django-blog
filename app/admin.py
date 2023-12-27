from django.db import models
from django.contrib import admin
from .models import Post, Tecnologia
from mdeditor.widgets import MDEditorWidget

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }
    list_display = ['titulo', 'autor']
    list_filter = ['titulo','tecnologias', 'autor']
    list_per_page = 10
    search_fields = ['titulo', 'tecnologias']
    view_on_site = True

admin.site.register(Post, PostAdmin)
admin.site.register(Tecnologia)