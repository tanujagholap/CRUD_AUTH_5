from django.urls import path
from .views import *


urlpatterns = [
    path('', create_view, name='create_url'),
    path('show/', show_view, name='show_url'),
    path('update/<int:pk>/', update_view, name='update_url'),
    path('delete/<int:pk>/', delete_view, name='delete_url'),
]
