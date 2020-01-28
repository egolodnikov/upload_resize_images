from io import BytesIO
from PIL import Image

from django.core.cache import cache
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import get_object_or_404

from .models import UploadImage


class ImageResizeHandler:
    """Create resize image and set in cache"""

    def __init__(self, req, pk):
        self.pk = pk
        self.image_object = get_object_or_404(UploadImage, pk=self.pk)
        if self.image_object.resize_image:
            self.size_object = self.image_object.resize_image.width, self.image_object.resize_image.height
        self.width = int(req.get('width')) if req.get('width') else self.image_object.image.width
        self.height = int(req.get('height')) if req.get('height') else self.image_object.image.height
        self.size = self.width, self.height

    def create_resize_image(self):
        # create resize image
        resize_image = None
        image_path = self.image_object.image.file
        image = Image.open(str(image_path))
        if self.width and self.height:
            resize_image = image.resize(
                self.size, Image.ANTIALIAS
            )
        elif self.height:
            resize_image = image.resize(
                self.size, Image.ANTIALIAS
            )
        elif self.width:
            resize_image = image.resize(
                self.size, Image.ANTIALIAS
            )
        buffer = BytesIO()
        resize_image.save(buffer, image.format)
        return ContentFile(buffer.getvalue())

    def save_in_model(self):
        # save in model and create cache
        resize_image_buffer = self.create_resize_image()
        file_name = f'{self.image_object.name}_{self.size}'
        print(file_name)
        if resize_image_buffer:
            self.image_object.resize_image.save(
                self.image_object.name,
                InMemoryUploadedFile(
                    # file
                    resize_image_buffer,
                    # field_name
                    None,
                    # file name
                    file_name,
                    # content type
                    'image/jpeg',
                    # size
                    resize_image_buffer.tell,
                    # content type extra
                    None
                ),
                save=False
            )
            self.image_object.save()
        cache.delete(self.pk)
        cache.set(
            self.pk,
            self.image_object.resize_image
        )

    def equal_size(self):
        # check size cache image and request args
        size = self.width, self.height
        if size == self.size_object:
            return True
        return False
