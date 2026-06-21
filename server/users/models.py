from django.db import models
from django.conf import settings

# Create your models here.
class Bookmark(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  article = models.ForeignKey('news.Articles', on_delete=models.CASCADE)
  saved_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields = ['user', 'article'],
        name= 'unique_bookmark'
        )
      ]