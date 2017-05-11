from django.contrib import admin

from .models import School, Campus, Study

class SchoolAdmin(admin.ModelAdmin):
        fields = ['school_id', 'school_name', 'school_info']
        
class CampusAdmin(admin.ModelAdmin):
        fields = ['campus_id', 'campus_name', 'campus_school_name', 'campus_info']
        
class StudyAdmin(admin.ModelAdmin):
        fields = ['study_id', 'study_name', 'study_school_name', 'study_campus_name', 'study_info']
        
admin.site.register(School, SchoolAdmin)        
admin.site.register(Campus, CampusAdmin)        
admin.site.register(Study, StudyAdmin)       