from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Exp(models.Model):
    place = models.CharField(max_length=255)
    web = models.URLField(null=True, blank=True)

    my_title = models.CharField(max_length=255)
    description = RichTextField()
    
    init_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.my_title


class Skills(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(null=True, blank=True)
    description = RichTextField()
    order = models.IntegerField()

    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=255)
    frontend_layout = models.BooleanField(null=True, blank=True)

    date = models.DateField()
    description = RichTextField()

    backend_gitHub = models.URLField(null=True, blank=True)
    gitHub = models.URLField(blank=True)
    live = models.URLField(blank=True)

    image = models.URLField(null=True, blank=True)
    
    skills = models.ManyToManyField(Skills, related_name="projects")

    def __str__(self):
        return self.name
