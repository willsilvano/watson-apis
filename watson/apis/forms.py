from django import forms

class TranslateForm(forms.Form):
    texto = forms.CharField(label='Texto', widget=forms.Textarea)