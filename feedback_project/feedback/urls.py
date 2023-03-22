from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('done', views.done),
    path('<int:id_feedback>', views.update_feedback),
]