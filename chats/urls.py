from django.urls import path

from .views import ChatListView, ChatDetailView, ChatCreateView, ChatEditView, ChatDeleteView

urlpatterns = [
    path('', ChatListView.as_view(), name='home'),
    path('chat/<int:pk>/delete', ChatDeleteView.as_view(), name='delete'),
    path('chat/<int:pk>/edit/', ChatEditView.as_view(), name='edit'),
    path('chat/new/', ChatCreateView.as_view(), name='chat_add'),
    path('chat/<int:pk>/', ChatDetailView.as_view(), name='detail'),
]
