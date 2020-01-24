from django.urls import path, include
from .views import sign_up, home

urlpatterns = [
    path('', home, name='home'),
    path('signup/', sign_up, name='signup')
]