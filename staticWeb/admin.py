from django.contrib import admin
from .models import Transcripts,Candidates,MyUser,Student,Peixunban,Enterprise

# Register your models here.
class TranscriptsAdmin(admin.ModelAdmin):
    list_display = ('stu_name','stu_clas','subject')
    search_fields = ('stu_name','subject',)
    fields = ('stu_name','stu_clas''subject')

class CandidatesAdmin(admin.ModelAdmin):
    list_display = ('title','pxban_name','enterprise_name','created_date')
    search_fields = ('titlee', 'enterprise_name')
    list_filter = ('created_date',)
    ordering = ('-created_date',)
    fields = ('title', 'pxban_name''enterprise_name','content','created_date','modify_date','is_show')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('username','stu_class','tele_num')
    search_fields = ('username','student_id')
    list_filter = ('date_joined',)
    ordering = ('-date_joined',)
    filter_horizontal = ('transcripts','candidates')

class PeixunbanAdmin(admin.ModelAdmin):
    list_display = ('peixun_name',)
    search_fields = ('peixun_name',)
    filter_horizontal = ('students','candidates')

class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('username','tele_num','date_joined')
    search_fields = ('username','tele_num')
    list_filter = ('date_joined',)
    ordering = ('-date_joined',)
    filter_horizontal = ('peixunban',)

admin.site.register(Transcripts,TranscriptsAdmin)
admin.site.register(Candidates,CandidatesAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Peixunban,PeixunbanAdmin)
admin.site.register(Enterprise,EnterpriseAdmin)