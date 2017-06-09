from django.contrib import admin

from .models import School, Campus, Study, Article

class SchoolAdmin(admin.ModelAdmin):
        fields = ['school_id', 'school_name', 'school_info']
        
class CampusAdmin(admin.ModelAdmin):
        fields = ['campus_id', 'campus_name', 'campus_school_name', 'campus_info', 'campus_image']
        list_display = ('campus_name', 'campus_school_name')
        
class StudyAdmin(admin.ModelAdmin):
        fields = ['study_id', 'study_name', 'study_school_name', 'study_campus_name', 'study_info']
        list_display = ('study_name', 'study_campus_name', 'study_school_name')
        
class ArticleAdmin(admin.ModelAdmin):
        fields = ['article_title', 'article_text', 'article_image', 'must_show']
        list_display = ('article_title', 'must_show')
        
admin.site.register(School, SchoolAdmin)        
admin.site.register(Campus, CampusAdmin)        
admin.site.register(Study, StudyAdmin)
admin.site.register(Article, ArticleAdmin)