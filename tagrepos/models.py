from django.db import models
from taggit.managers import TaggableManager

class Repository(models.Model):
    repo_url = models.URLField(max_length=300)
    tags = TaggableManager()
    short_description = models.CharField(max_length=80)
    long_description = models.CharField(max_length=500,null=True)