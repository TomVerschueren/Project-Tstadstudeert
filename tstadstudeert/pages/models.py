from __future__ import unicode_literals

from django.db import models


class School(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=100)
    def __str__(self):
        return self.school_name

    
class Campus(models.Model):
    campus_id = models.CharField(max_length=100)
    campus_name = models.CharField(max_length=100)
    campus_school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    def __str__(self):
        return self.campus_name
    
    class Meta:
        verbose_name_plural = "Campuses"

class Study(models.Model):
    study_id = models.IntegerField()
    study_name = models.CharField(max_length=100)
    study_school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    study_campus_name = models.ForeignKey(Campus, on_delete=models.CASCADE)
    def __str__(self):
        return self.study_name
    
    class Meta:
        verbose_name_plural = "Studies"
    
    
class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_nickname = models.CharField(max_length=100)
    user_lastname = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    user_campus_name = models.ForeignKey(Campus, on_delete=models.CASCADE)
    user_study_name = models.ForeignKey(Study, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_nickname 
    
    
