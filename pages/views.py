from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Pages 
# Create your views here.

class PageListView(ListView):
    model = Pages 
    template_name = "home.html"
    context_object_name = "pages"

class PageDetailView(DetailView):
    model = Pages 
    template_name = "detail_page.html"
    context_object_name = "page"