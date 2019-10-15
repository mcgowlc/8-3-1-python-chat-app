
urlpatterns[
    path('', ChatListView.as_view(), name='home'),
    path('chat/<int:pk>/delete', ChatDeleteView.as_view(), name='chat_delete'),
    path('chat/<int:pk>/edit/', ChatEditView.as_view(), name='chat_edit'),
    path('chat/new/', ChatCreateView.as_view(), name='chat_new'),
]
