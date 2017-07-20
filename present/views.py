from django.shortcuts import render

def index(request):
   d = {'d': 100 }
   return render(request, 'details.html', d) 
