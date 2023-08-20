from django.urls import path
from .views import AdsList, AdsDetailView


urlpatterns = [
    path('', AdsList.as_view(), name='main_page'),
    path('<int:pk>', AdsDetailView.as_view(), name='ad'),
]