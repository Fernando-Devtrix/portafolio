from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(default="content")
    image = models.ImageField(upload_to="projects")
    link = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    # class Meta:
    #     verbose_name = "proyecto"
    #     verbose_name_plural = "proyectos"
    #     ordering = ["-created"]
    
    def __str__(self):
      return self.title

