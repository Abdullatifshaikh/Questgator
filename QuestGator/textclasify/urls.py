from django.urls import path
from . import views
from .views import classify
urlpatterns = [
    path('', classify , name='classify'),
]