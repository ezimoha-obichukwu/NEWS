from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


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
    

@receiver(post_save, sender=User)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)