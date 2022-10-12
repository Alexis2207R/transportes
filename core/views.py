from django.shortcuts import render

# Create your views here.

def reportes(request):
    return render(request, "core/reportes.html")
