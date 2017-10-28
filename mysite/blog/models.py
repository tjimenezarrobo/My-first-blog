from django.db import models
from django.utils import timezone
class Post (models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models. TextField()
def published(self):
    self.published_date = timezone.now()
    self.save()
def _str_(self):
    return self.title





# Create your models here.
