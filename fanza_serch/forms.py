from django import forms


class SeachForm(forms.Form):
    name = forms.CharField(required=False, max_length=10)
    cup = forms.CharField(required=False, max_length=1)
    max_height = forms.CharField(required=False, max_length=3)
    min_height = forms.CharField(required=False, max_length=3)
