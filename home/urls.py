from django.urls import path

from home.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home')
]
