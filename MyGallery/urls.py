from django.urls import path
from .views import display_image

urlpatterns = [
    path("", display_image, name="home")
]