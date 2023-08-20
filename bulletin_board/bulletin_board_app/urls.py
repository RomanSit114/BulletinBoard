from django.urls import path
from .views import AdsList  # импортируем наше представление


urlpatterns = [
    path('', AdsList.as_view()),
]