from django.urls import path
from .views import add_review

urlpatterns = [
    path('write/<slug:slug>', add_review, name='add_review'),
]
