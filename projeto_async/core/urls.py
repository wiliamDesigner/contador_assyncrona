from django.urls import path
from .views import contador

urlpatterns = [
    path('contador/', contador),
]
