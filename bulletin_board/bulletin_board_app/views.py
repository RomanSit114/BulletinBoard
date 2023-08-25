from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ad
from django.template.loader import render_to_string
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import AdsForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

class AdsList(ListView):
    model = Ad
    template_name = 'bulletin_board_app/ads.html'
    context_object_name = 'ads'
    ordering = ['-id']
    paginate_by = 10

class MyAdsList(LoginRequiredMixin, ListView):
    model = Ad
    template_name = 'bulletin_board_app/my_ads.html'
    context_object_name = 'ads'
    ordering = ['-id']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.username:
            user_ads = Ad.objects.filter(author=self.request.user.id)
            context['ads'] = user_ads
        return context

class AdsDetailView(DetailView):
    model = Ad
    template_name = 'bulletin_board_app/ad.html'
    context_object_name = 'ad'
    queryset = Ad.objects.all()

class AdsCreateView(LoginRequiredMixin, CreateView):
# @login_required
# @method_decorator(login_required, name='dispatch')
# class AdsCreateView(CreateView):
    # permission_required = ('newapp.add_post')
    form_class = AdsForm
    template_name = 'bulletin_board_app/ad_create.html'
    # success_url = '/ads/'


    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['author'].widget = forms.HiddenInput()  # Скрываем поле выбора автора
    #     return form

    def form_valid(self, form):
        # Устанавливаем автора объявления в текущего пользователя
        form.instance.author = self.request.user
        return super().form_valid(form)

class AdsUpdateView(LoginRequiredMixin, UpdateView):
    # permission_required = ('newapp.add_post')
    form_class = AdsForm
    template_name = 'bulletin_board_app/ad_create.html'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)

class AdsDeleteView(LoginRequiredMixin, DeleteView):
   template_name = 'bulletin_board_app/ad_delete.html'
   queryset = Ad.objects.all()
   success_url = '/ads/'
