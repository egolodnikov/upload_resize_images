from django.urls import path

from .views import UploadImageDetailView


urlpatterns = [
    path('image/<int:pk>/', UploadImageDetailView.as_view(), name='image-detail')
]
