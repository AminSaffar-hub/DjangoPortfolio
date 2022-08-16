from django.db import models
from distutils.command.upload import upload

from django.db import models
from ckeditor.fields import RichTextField


class PersonalInformation(models.Model):
    name_complete = models.CharField(max_length=50, blank=True, null=True)
    job_name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='images/', null=True)
    mini_about = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    cv = models.FileField(upload_to='cv', blank=True, null=True)

    def __str__(self):
        return self.name_complete


class About(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description1 = models.TextField(blank=False, null=True)
    description2 = models.TextField(blank=False, null=True)
    about_avatar = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    skill = models.TextField(max_length=230, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):

    full_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)

    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    skill_name = models.CharField(max_length=50, blank=True, null=True)

    class MasteryLvlTypes(models.TextChoices):
        BASIC_UNDERSTANDING = "Basic understandig"
        INTERMEDIATE = "Intermediate"
        FLUENT = "Fluent"
        CREATIVE = "Creative"
        MASTERY = "Master"

    mastery_level_string = models.CharField(max_length=20, choices=MasteryLvlTypes.choices, 
        default=MasteryLvlTypes.BASIC_UNDERSTANDING)

    mastery_level_percentage = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.skill_name
