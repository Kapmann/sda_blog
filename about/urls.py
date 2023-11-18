from django.urls import path
from .views import about


urlspatterns = [
    path("", about, name="about")

]