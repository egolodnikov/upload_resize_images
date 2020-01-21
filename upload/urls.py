from django.urls import path

from home.views import UploadTemplateView

urlpatterns = [
    path('upload/', UploadTemplateView.as_view(), name='upload')
]
