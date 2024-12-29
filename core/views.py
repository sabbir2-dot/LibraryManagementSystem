from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from authentication.models import Book
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

class BookDetails(DetailView):
    model = Book
    template_name = 'book_details.html'