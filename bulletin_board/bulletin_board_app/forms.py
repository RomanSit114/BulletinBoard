from django.forms import ModelForm
from .models import Ad

class AdsForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'text', 'adCategory', 'image', 'video', 'file']
