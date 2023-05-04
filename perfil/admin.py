

from django.contrib import admin

from .models import Project

@admin.register(Project) 
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'created') 
    list_editable = ('title',) 
    list_filter = ('title', 'created', 'updated')
    search_fields =('title',)

