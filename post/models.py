from django.db import models

from user.models import User
from gallery.models import Album

import datetime


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    photo = models.ImageField(upload_to="image/user")
    content = models.TextField(max_length=1024, default="Content")
    comment = models.TextField(max_length=1024, default="Comment")
    views = models.IntegerField(default=0)
    thumbs = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    modified_at = models.DateTimeField(auto_now=True)


class Problem(models.Model):
    CATEGORY = (
        ("SITE", "Site"),
        ("USER", "User"),
        ("IMAGE", "Image"),
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    photo = models.ForeignKey(Album, on_delete=models.CASCADE)
    category = models.CharField(max_length=12, choices=CATEGORY, default="SITE")
    content = models.TextField(max_length=1024, default="Content")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    modified_at = models.DateTimeField(auto_now=True)