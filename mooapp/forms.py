from django import forms
from mooapp.models import Cow

class MooForm(forms.Form):
    said = forms.CharField(max_length=180)