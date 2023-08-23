from django.forms import ModelForm
from .models import Ad

class AdsForm(ModelForm):
    class Meta:
        model = Ad
        # exclude = ['author']
        # fields = ['author', 'title', 'text', 'adCategory']
        fields = ['title', 'text', 'adCategory', 'image', 'file']
        # fields = ['title', 'text', 'adCategory']

