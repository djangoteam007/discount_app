from urllib.parse import urlparse
from django.urls import path
from .views import index

urlpatterns=[
    path('',index),
]