from django.db import models

# Create your models here.
class image_projet(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='media/')