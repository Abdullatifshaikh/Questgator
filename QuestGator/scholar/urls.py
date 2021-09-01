from django.urls import path
from . import views
urlpatterns = [
    path('', views.scholar, name='scholar'),
]