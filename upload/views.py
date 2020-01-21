from django.views.generic import TemplateView


class UploadTemplateView(TemplateView):
    template_name = 'upload/upload.html'
