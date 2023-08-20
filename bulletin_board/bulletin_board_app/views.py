from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ad
from django.template.loader import render_to_string
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect

class AdsList(ListView):
    model = Ad
    template_name = 'bulletin_board_app/ads.html'
    context_object_name = 'ads'

class AdsDetailView(DetailView):
    model = Ad
    template_name = 'bulletin_board_app/ad.html'
    context_object_name = 'ad'
    queryset = Ad.objects.all()
