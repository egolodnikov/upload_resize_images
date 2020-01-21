from django.urls import path

from .views import UploadTemplateView

urlpatterns = [
    path('upload/', UploadTemplateView.as_view(), name='upload')
]
