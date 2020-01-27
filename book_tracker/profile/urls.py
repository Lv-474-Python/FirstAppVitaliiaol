from django.urls import path
from .views import view_profile, edit_profile, change_password

urlpatterns = [
    path('', view_profile, name='profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),
]
