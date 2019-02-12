from django.db import models
from PIL       import Image , ImageFile

class Photo(models.Model):
    File  = models.ImageField()
    def edit(self):
        return Image.open(self.File.file.file)

class Shared_Photos(models.Model):
    shared_photos = models.ImageField()
    others        = models.BooleanField(default = True)
    session_key   = models.TextField(default = "1")