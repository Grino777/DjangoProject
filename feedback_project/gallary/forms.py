from django import forms


class GallaryForm(forms.Form):
    image = forms.FileField(label='Файл', error_messages={'required': 'Загрузите файл',})
