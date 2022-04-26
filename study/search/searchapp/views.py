from django.shortcuts import render
from django import forms
from requests import post, request
from django.db.models import Q
from .models import Building
from django.views.generic import TemplateView, ListView
# Create your views here.
class Search(TemplateView):
    template_name= 'search.html'

class Result(ListView):
    model = Building
    template_name = 'result.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Building.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query)
        )
        return object_list