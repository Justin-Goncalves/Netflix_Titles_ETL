from .views import *
from django.urls import path
urlpatterns = [
    path("", streamingcontent_details),
]