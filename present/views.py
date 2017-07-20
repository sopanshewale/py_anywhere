from django.shortcuts import render

def index(request):
   d = {'d': 100 }
   return render(request, 'templates/details.html', d) 
