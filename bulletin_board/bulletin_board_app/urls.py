from django.urls import path
from .views import AdsList,MyAdsList, AdsDetailView, AdsCreateView, AdsUpdateView, AdsDeleteView

# app_name = 'bulletin_board_app'
urlpatterns = [
    path('', AdsList.as_view(), name='main_page'),
    path('ad/<int:pk>', AdsDetailView.as_view(), name='ad'),
    path('my_ads/', MyAdsList.as_view(), name='my_ads'),
    path('ad/create/', AdsCreateView.as_view(), name='ad_create'),
    path('ad/update/<int:pk>/', AdsUpdateView.as_view(), name='ad_update'),
    path('ad/delete/<int:pk>/', AdsDeleteView.as_view(), name='ad_delete'),
]
