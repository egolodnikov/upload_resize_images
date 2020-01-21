from django.db import models


class UploadImage(models.Model):
    name = models.CharField(
        max_length=30
    )
    width = models.PositiveSmallIntegerField(
        default=0
    )
    height = models.PositiveSmallIntegerField(
        default=0
    )
    url = models.URLField()
    image = models.ImageField(
        upload_to='images/'
    )

