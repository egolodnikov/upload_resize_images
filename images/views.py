from django.views.generic import DetailView

from images.models import UploadImage


class UploadImageDetailView(DetailView):
    model = UploadImage
    template_name = 'upload/detail.html'

