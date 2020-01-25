from django.urls import path, include
from .views import home, sign_up, sign_in, sign_out

urlpatterns = [
    path('', home, name='home'),
    path('signup/', sign_up, name='signup'),
    path('signin/', sign_in, name='signin'),
    path('signout', sign_out, name='signout')
]