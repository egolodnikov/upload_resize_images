import requests

from ur_images.settings import MEDIA_ROOT
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from images.models import UploadImage
from upload.forms import UploadImageForm


class ImageCreateView(FormView):
    form_class = UploadImageForm
    template_name = 'home/home.html'
    success_url = reverse_lazy('upload')

    def form_valid(self, form):
        if form.cleaned_data['url']:
            # splice name
            image_name = form.cleaned_data['url'].split('/')[-1].split('?')[0]
            # create symlink in file system
            file_storage = f'{MEDIA_ROOT}/images/{image_name}'
            # create symlink in images/
            image_storage = f'images/{image_name}'
            # create, write img_file in images/ and download image
            f = open(file_storage, 'wb')
            image_data = requests.get(form.cleaned_data['url'])
            f.write(image_data.content)
            f.close()
            # create img object and save
            image = UploadImage.objects.create(
                name=image_name,
                image=image_storage
            )
        elif form.data['image']:
            name = form.data['image']
            image_storage = f'images/{name}'
            image = UploadImage.objects.create(
                name=name,
                image=image_storage
            )
        return HttpResponseRedirect(
            reverse_lazy(
                'upload'
            )
        )

