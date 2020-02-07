from django.urls import path
from .views import add_to_log, view_log, delete_log

urlpatterns = [
    path('add/<slug:slug>', add_to_log, name='add_to_log'),
    path('view_log/', view_log, name='view_log'),
    path('delete/<int:log_id>/', delete_log, name='delete_log')
]
