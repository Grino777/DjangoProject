from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, TemplateView, ListView
from django.urls import reverse
from .forms import FeedbackForm
from .models import Feedback

from django.views import View


# Create your views here.

class FeedbackView(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback/index.html', context={'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                form.save()
                return HttpResponseRedirect('/done')
            else:
                return render(request, 'feedback/index.html', context={'form': form})

# def index(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # feed = Feedback(
#             #     name=form.cleaned_data['name'],
#             #     surname=form.cleaned_data['surname'],
#             #     feedback=form.cleaned_data['feedback'],
#             #     rating=form.cleaned_data['rating'],
#             # ).save()
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback/index.html', context={'form': form})

class DoneView(TemplateView):
    template_name = 'feedback/done.html'

# def done(request):
#     return render(request, 'feedback/done.html')

class UpdateFeedbackView(View):
    def get(self, request, id_feedback):
        feed = get_object_or_404(Feedback, id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/index.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = get_object_or_404(Feedback, id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        else:
            form = FeedbackForm(request.POST, instance=feed)
        return render(request, 'feedback/index.html', context={'form': form})

# def update_feedback(request, id_feedback):
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm(instance=feed)
#     return render(request, 'feedback/index.html', context={'form': form})

# class FeedbacksView(TemplateView):
#     template_name = 'feedback/feedbacks.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feedbacks'] = Feedback.objects.all()
#         return context

class DetailFeedback(DetailView):
    template_name = 'feedback/feedback_info.html'
    model = Feedback
    context_object_name = 'feedback'




class ListFeedbackView(ListView):
    template_name = 'feedback/feedbacks.html'
    model = Feedback
    context_object_name = 'feedbacks'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-rating')
        return queryset

