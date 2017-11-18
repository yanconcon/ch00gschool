from django.contrib import admin
from .models import Student, Company, Cours

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username','date_joined','phone')
    search_fields = ('username',)
    list_filter = ('date_joined',)
    ordering = ('-date_joined',)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('username','date_joined','phone')
    search_fields = ('username',)
    list_filter = ('date_joined',)
    ordering = ('-date_joined',)

class CoursAdmin(admin.ModelAdmin):
    list_display = ('lesson_name','cmpany_associated')
    search_fields = ('lesson_name',)
    list_filter = ('release_time',)
    ordering = ('-release_time',)
    filter_horizontal = ('student',)


admin.site.register(Student,StudentAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Cours,CoursAdmin)
