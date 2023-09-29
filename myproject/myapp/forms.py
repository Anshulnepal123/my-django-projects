from django import forms
from tinymce.models import HTMLField


class userForms(forms.Form):
    name = forms.CharField()
    pw = forms.Textarea()