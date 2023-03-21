from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={"cols": "30", "rows": "7"}))