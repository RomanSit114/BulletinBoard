from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.template.loader import render_to_string
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import *
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

# class AdsComments(DetailView):
#     model = Ad
#     template_name = 'bulletin_board_app/ad.html'
#     context_object_name = 'ad'
#     queryset = Ad.objects.all()

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'bulletin_board_app/comment_create.html'
    # success_url = '/success-url/'

    def form_valid(self, form):
        ad_id = self.kwargs['pk']
        ad = Ad.objects.get(pk=ad_id)
        comment = form.save(commit=False)
        comment.commentAuthor = self.request.user
        comment.save()
        ad.comments.add(comment)
        comment_text = form.cleaned_data['text']
        ad_owner_email = ad.author.email

        html_content = render_to_string(
            'bulletin_board_app/new_comment_email.html',
            {
                'comment_text': comment_text,
                'ad': ad,
                'comment_author': comment.commentAuthor,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f"Новый отклик на ваше объявление '{ad.title}'",
            body=f"Здравствуйте!\n\nНа ваше объявление поступил новый отклик от пользователя {comment.commentAuthor}",
            from_email='roma.sitdikov@yandex.ru',
            to=[ad_owner_email],
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html
        msg.send()  # отсылаем
        # print(html_content)

        return super().form_valid(form)

class CommentsOnMyAdsList(LoginRequiredMixin, ListView): # представление, для отображения откликов, котороые оставили другие пользователи на мои объявления
    model = Ad
    template_name = 'bulletin_board_app/comments_on_my_ads.html'
    context_object_name = 'ads'
    # queryset = Ad.objects.all()
    ordering = ['-id']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ads_by_current_user = Ad.objects.filter(author=self.request.user) # чтобы на странице показывались только объявления авторизованного пользователя
        user_has_ads = ads_by_current_user.exists() # проверка на то, создавал ли авторизованный на данный момент пользователь хотя бы одно объявления
        context['user_has_ads'] = user_has_ads
        context['ads_by_current_user'] = ads_by_current_user

        ads_with_comments = []
        for ad in context['ads_by_current_user']:
            if ad.comments.exists():  # Проверка наличия комментариев у объявления
                ads_with_comments.append(ad)

        context['ads_with_comments'] = ads_with_comments
        return context
