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
    url = models.URLField(
        max_length=100,
        blank=True
    )
    image = models.ImageField(
        upload_to='images/'
    )
    resize_image = models.ImageField(
        blank=True
    )

    def __str__(self):
        return self.name

