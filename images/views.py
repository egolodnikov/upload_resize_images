from PIL import Image
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.urls import reverse

from django.views.generic import DetailView

from ur_images.settings import MEDIA_ROOT, MEDIA_URL
from .models import UploadImage

from upload.forms import ImageDetailViewForm


class UploadImageDetailView(DetailView):
    model = UploadImage
    form_class = ImageDetailViewForm
    template_name = 'upload/detail.html'

    def get(self, request, *args, **kwargs):
        req: dict = request.GET.copy()
        if req['width'] and req['height']:
            resize_image = cache.get('resize_image')
            print('cache')
            if resize_image is None:
                print('nocache')
                image_object: object = get_object_or_404(UploadImage, pk=self.kwargs['pk'])
                if image_object:
                    image_object.resize_images = '1'
                    # image_object.save()
                # image_object.update('')
                print(image_object)
                image_path: str = get_object_or_404(UploadImage, pk=self.kwargs['pk']).image.file.name
                image = Image.open(image_path)
                w: int = int(req['width'])
                h: int = int(req['height'])
                resize_image = image.resize((w, h), Image.ANTIALIAS)
                path_resize_image = 'images/resize_image.jpeg'
                relative_path_resize_image = f'{MEDIA_URL}{path_resize_image}'
                resize_image.save(f'{MEDIA_ROOT}/{path_resize_image}')
                cache.set('resize_image', relative_path_resize_image)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('image-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # cache.delete('resize_image')
        context['resize_image'] = cache.get('resize_image')
        context['form'] = ImageDetailViewForm()
        return context
