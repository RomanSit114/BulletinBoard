from django.forms import ModelForm
from .models import Ad

class AdsForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['author', 'title', 'text', 'adCategory']
        # fields = ['title', 'text', 'adCategory']

