from django.urls import path
from .views import add_review, update_review

urlpatterns = [
    path('write/<slug:slug>', add_review, name='add_review'),
    path('update/<slug:slug>', update_review, name='update_review'),
]
