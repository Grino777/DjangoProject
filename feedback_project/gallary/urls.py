from django.urls import path
from . import views

urlpatterns = [
    path('load_image', views.CreateGallaryView.as_view()),
]