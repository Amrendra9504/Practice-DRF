from django.shortcuts import render
from rest_framework.views import APIView
from CityChoice.models import City
from .forms import ProfileForm

from django.views.generic import ListView

# class CityList(APIView):
#     def get(self, request):
#         form = ProfileForm(request.POST)
#         print("m here in choice")
#         import pdb
#         pdb.set_trace()

class CityList(ListView):
    def get(self, request):
        model = City
        print("in model")
        import pdb 
        pdb.set_trace()