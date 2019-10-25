from django.contrib import admin
from .models import Student, Part, Branch

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'family_name', 'university', 'part', 'branch', 'publish')
    list_filter = ('publish',)
    ordering = ['-publish']

    
admin.site.register(Student,StudentAdmin)
admin.site.register(Part)
admin.site.register(Branch)