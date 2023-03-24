from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackView.as_view()),
    path('<int:id_feedback>', views.UpdateFeedbackView.as_view()),
    path('done', views.DoneView.as_view()),
    path('feedback/<int:pk>', views.DetailFeedback.as_view()),
    path('update/<int:pk>', views.FeedbackViewUpdate.as_view()),
    path('feedbacks', views.ListFeedbackView.as_view()),
]