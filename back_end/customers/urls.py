from django.urls import path, include
from .api import RegisterCustomerAPI
from knox import views as knox_views

urlpatterns = [
    path('api/auth/customer', include('knox.urls')),
    path('api/auth/customer/register', RegisterCustomerAPI.as_view())
]