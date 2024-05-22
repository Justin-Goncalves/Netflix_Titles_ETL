from .views import *
from django.urls import path
urlpatterns = [
    path("", StreamingContent_details),
]