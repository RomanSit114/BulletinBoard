from django.urls import path
from .views import AdsList, MyAdsList, AdsDetailView, AdsCreateView, AdsUpdateView, AdsDeleteView, CommentCreateView, CommentsOnMyAdsList
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'bulletin_board_app'
urlpatterns = [
    path('', AdsList.as_view(), name='main_page'),
    path('ad/<int:pk>', AdsDetailView.as_view(), name='ad'),
    path('my_ads/', MyAdsList.as_view(), name='my_ads'),
    path('ad/create/', AdsCreateView.as_view(), name='ad_create'),
    path('ad/update/<int:pk>/', AdsUpdateView.as_view(), name='ad_update'),
    path('ad/delete/<int:pk>/', AdsDeleteView.as_view(), name='ad_delete'),
    path('ad/create_comment/<int:pk>/', CommentCreateView.as_view(), name='comment_create'),
    path('comments_on_my_ads/', CommentsOnMyAdsList.as_view(), name='comments_on_my_ads'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
