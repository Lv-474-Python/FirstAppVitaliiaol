from django.urls import path
from .views import add_to_log

urlpatterns = [
    path('add/<slug:slug>', add_to_log, name='add_to_log')
]
