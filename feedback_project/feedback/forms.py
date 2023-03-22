from django import forms

from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
#         'max_lenght': 'Слишком много символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.',
#         'min_length': 'Слишком мало символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.',
#         'required': 'Поле не заполнено',
#     })
#     surname = forms.CharField(label='Фамилия')
#     feedback = forms.CharField(widget=forms.Textarea(attrs={"cols": "20", "rows": "2"}), label='Отзыв')
#     rating = forms.IntegerField(label='Рейтинг', min_value=1, max_value=5)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'surname', 'feedback', 'rating']
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтиг',
        }
        error_messages = {
            'name': {
                'max_lenght': 'Слишком много символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.',
                'min_length': 'Слишком мало символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.',
                'required': 'Поле не заполнено',
            },
            'surname': {
                'max_lenght': 'Слишком много символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.',
                'min_length': 'Слишком мало символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.',
                'required': 'Поле не заполнено',
            },
            'rating': {
                'max_lenght': 'Рейтинг должен быть от 1 до 5',
                'min_length': 'Рейтинг должен быть от 1 до 5',
                'required': 'Поле не заполнено',
            }
        }
