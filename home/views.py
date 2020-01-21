from django.views.generic import ListView, TemplateView

from images.models import UploadImage


class HomeListView(ListView):
    """main page
    List of all images
    """
    model = UploadImage
    template_name = 'home/home.html'
