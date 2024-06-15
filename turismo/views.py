from django.shortcuts import render
from .models import Servicio

# Create your views here.
def index(request):
    context={}
    return render(request,'turismo/index.html',context)

def servicios(request):
    servicio= Servicio.objects.all()
    context={"servicios":servicio}
    return render(request,'turismo/servicios.html',context)