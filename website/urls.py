from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('record/<str:pk>/', customer_record, name='record'),
    path('delete_record/<str:pk>/', delete_record, name='delete_record'),
    path('add_record/', add_record, name='add_record'),
    path('update_record/<str:pk>/', update_record, name='update_record'),
]
