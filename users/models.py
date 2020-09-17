from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

def upload_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return 'users/{0}/images/{1}'.format(instance.username, filename)


class UserProfile(AbstractUser):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    profile_picture = models.ImageField(blank=True, upload_to=upload_image_path)
    profession = models.CharField(max_length=254, blank=True)
    address = models.CharField(max_length=254, blank=True)
    dob = models.DateField(blank=True, null=True)
    donate = models.CharField(max_length=254, blank=True)
    fb_username = models.CharField(max_length=254, blank=True)
    tw_username = models.CharField(max_length=254, blank=True)
    in_username = models.CharField(max_length=254, blank=True)


class BannedUsernames(models.Model):
    uname = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = 'Banned Usernames'

    def __str__(self):
        return self.uname