from django.core.cache import cache
from django.urls import reverse

from django.views.generic import DetailView

from images.core import ImageResizeHandler
from .models import UploadImage

from .forms import ImageDetailViewForm


class UploadImageDetailView(DetailView):
    model = UploadImage
    form_class = ImageDetailViewForm
    template_name = 'upload/detail.html'

    def get(self, request, *args, **kwargs):
        req = request.GET.copy()
        pk_object = self.kwargs['pk']
        resize = ImageResizeHandler(req, pk_object)
        cache_object = cache.get(pk_object)
        if not cache_object:
            resize.create_resize_image()
            resize.save_in_model()
        else:
            if resize.image_object.resize_image:
                if not resize.equal_size():
                    resize.create_resize_image()
                    resize.save_in_model()
            else:
                resize.create_resize_image()
                resize.save_in_model()
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('image-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resize_image'] = cache.get(self.kwargs['pk'])
        context['form'] = ImageDetailViewForm()
        return context
