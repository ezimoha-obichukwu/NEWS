from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    image = models.ImageField(upload_to="news_images", blank=True ,null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    dte_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
    
