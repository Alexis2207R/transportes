from django.shortcuts import render
from materiales.models import Material

def reportes(request):
    materiales = Material.objects.all()
    return render(request, "core/reportes.html", {'materiales':materiales})