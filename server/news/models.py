from django.db import models

# Create your models here.
class Source(models.Model):
  name = models.CharField(max_length=30)
  slug = models.SlugField(max_length=100, unique=True)
  url = models.URLField(unique=True)
  rss_url = models.URLField(unique=True)
  is_active = models.BooleanField()
  
  def __str__(self):
    return self.name
    
    
class Category(models.Model):
  name= models.CharField(max_length=30)
  slug=models.SlugField()
  
  def __str__(self):
    return self.name
    
class Articles(models.Model):
  title = models.CharField(max_length=100)
  summary = models.TextField()
  url = models.URLField()
  image = models.URLField()
  #image = models.ImageField(upload_to="featured/")
  published_at = models.DateField(auto_now_add=True)
  source= models.ForeignKey(Source, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
    
