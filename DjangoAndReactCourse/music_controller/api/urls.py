from django.urls import path
from .views import main, homepage

urlpatterns = [
    path('', homepage),
    path('main',  main),
]
