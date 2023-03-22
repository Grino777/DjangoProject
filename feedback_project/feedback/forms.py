from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
        'max_lenght': 'Слишком много символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.',
        'min_length': 'Слишком мало символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.',
        'required': 'Поле не заполнено',
    })
    surname = forms.CharField(label='Фамилия')
    feedback = forms.CharField(widget=forms.Textarea(attrs={"cols": "30", "rows": "10"}), label='Отзыв')
    rating = forms.IntegerField(label='Рейтинг', min_value=1, max_value=5)