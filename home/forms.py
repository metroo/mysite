from django import forms

class TodoCreateFrom(forms.Form):
    title = forms.CharField(required=False , label='عنوان')
    body = forms.CharField()
    created = forms.DateTimeField()

