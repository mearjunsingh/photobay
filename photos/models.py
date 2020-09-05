from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

def upload_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return '{0}/{1}'.format(instance.user.username, filename)


class Photo(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_path)
    image_type = models.CharField(max_length=10)
    camera = models.ForeignKey('Camera', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    tags = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    modified_on = models.DateTimeField(auto_now=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        p_name = self.title[:10]
        p_user = self.user.username
        p_str = f'{p_name} - {p_user}'
        return p_str


class Category(models.Model):
    category = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category


class Camera(models.Model):
    camera = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.camera


class Location(models.Model):
    location = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.location