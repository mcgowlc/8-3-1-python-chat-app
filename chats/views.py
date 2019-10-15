from django.views.generic import ListView, DetailView
from .models import Chat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ChatListView(ListView):
    model = Chat
    template_name = 'home.html'
    context_object_name = 'chat_list'


class ChatEditView(UpdateView):
    model = Chat
    template_name = 'edit.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('home')


class ChatDeleteView(DeleteView):
    model = Chat
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


class ChatCreateView(CreateView):
    model = Chat
    template_name = 'chat_add.html'
    fields = ['title', 'text', 'author']


class ChatDetailView(DetailView):
    model = Chat
    template_name = 'detail.html'
