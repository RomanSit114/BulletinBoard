from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ad
from django.template.loader import render_to_string
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import AdsForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class AdsList(ListView):
    model = Ad
    template_name = 'bulletin_board_app/ads.html'
    context_object_name = 'ads'
    ordering = ['-id']
    paginate_by = 10

class AdsDetailView(DetailView):
    model = Ad
    template_name = 'bulletin_board_app/ad.html'
    context_object_name = 'ad'
    queryset = Ad.objects.all()

class AdsCreateView(CreateView):
    # permission_required = ('newapp.add_post')
    form_class = AdsForm
    template_name = 'bulletin_board_app/ad_create.html'
    # success_url = '/ads/'

class AdsUpdateView(UpdateView):
    # permission_required = ('newapp.add_post')
    form_class = AdsForm
    template_name = 'bulletin_board_app/ad_create.html'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)

class AdsDeleteView(DeleteView):
   template_name = 'bulletin_board_app/ad_delete.html'
   queryset = Ad.objects.all()
   success_url = '/ads/'
