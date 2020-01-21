from django.views.generic import ListView, TemplateView


class HomeTemplateView(TemplateView):
    """main page
    List of all images
    """
    template_name = 'home/home.html'
