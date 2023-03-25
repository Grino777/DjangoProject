from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackView.as_view()),
    path('done', views.DoneView.as_view()),
    path('feedback/<int:pk>', views.DetailFeedback.as_view(), name='feedback_info'),
    path('update/<int:pk>', views.FeedbackUpdateView.as_view(), name='update_feedback'),
    path('feedbacks', views.ListFeedbackView.as_view()),
]