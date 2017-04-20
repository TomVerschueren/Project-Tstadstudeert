from django.contrib import admin

from .models import School, Campus, Study, User

class SchoolAdmin(admin.ModelAdmin):
        fields = ['school_id', 'school_name']
        
class CampusAdmin(admin.ModelAdmin):
        fields = ['campus_id', 'campus_name', 'campus_school_name']
        
class StudyAdmin(admin.ModelAdmin):
        fields = ['study_id', 'study_name', 'study_school_name', 'study_campus_name']
        
class UserAdmin(admin.ModelAdmin):
        fields = ['user_id', 'user_name', 'user_nickname', 'user_lastname', 'user_password', 'user_school_name', 'user_campus_name', 'user_study_name']
        
admin.site.register(School, SchoolAdmin)        
admin.site.register(Campus, CampusAdmin)        
admin.site.register(Study, StudyAdmin)        
admin.site.register(User, UserAdmin)        