from django.urls import path
from . import views
urlpatterns = [
    path('', views.scholarships, name='scholarships'),
]