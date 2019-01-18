from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from books.models import Book

# Create your views here.


class BookList(ListView):
    model = Book


class BookView(DetailView):
    model = Book


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')


class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')