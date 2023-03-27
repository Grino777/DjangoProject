from django.views.generic import CreateView

from .forms import GallaryForm
from .models import Gallary


# Create your views here.

# def storage_file(file: InMemoryUploadedFile):
#     '''Функция для записи файла.'''
#     with open(f'gallary_tmp/{file.name}', 'wb+') as new_file:
#         for chunk in file.chunks():
#             new_file.write(chunk)


class CreateGallaryView(CreateView):
    template_name = 'gallary/load_file.html'
    model = Gallary
    success_url = 'load_file.html'
    fields = '__all__'
    # form_class = GallaryForm #используется когда форма наследуется от модели



# class GallaryView(View):
#     def get(self, request):
#         '''Отображение формы на при get-запросе.'''
#         form = GallaryForm()
#         return render(request, 'gallary/load_file.html', context={'form': form})
#
#     def post(self, request):
#         '''Обработка данных с формы.'''
#         form = GallaryForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_image = Gallary(image=form.cleaned_data['image'])
#             new_image.save()
#             return HttpResponseRedirect('load_image')
#         return render(request, 'gallary/load_file.html', context={'form': form})
