from .models import Empleado, Empresa, Asesor, nomYSs, modelo111190, User
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django import forms
from datetime import datetime
from django.db.models import Q
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

now = datetime.now()
# Create your views here.
def index(request):
    return render(request, 'nucleo/index.html', {})

@login_required(login_url='/accounts/login/')
def Empleados(request):
    queryset = request.GET.get("buscar")
    empleados=Empleado.objects.filter(oculto = False)
    if queryset:
        empleados = Empleado.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(fecha__icontains = queryset) 
        ).distinct
    hoy=now.date()
    empl = Empleado.objects.filter(fin=False, fecha__lte=hoy)
    for em in empl:
        messages.info(request, 'ATENCIÓN '+em.empresa.asesor+'! El trabajador '+em.nombre+' ha vencido la fecha establecida')
        
    return render(request, "nucleo/empleados.html", {'empleados':empleados, 'hoy':hoy})

@method_decorator([login_required], name='dispatch')
class EmpleadoCreateView(CreateView):
    model=Empleado
    fields=['nombre','empresa', 'tipo_vencimiento', 'fecha']
   
    success_url="/empleados" 

@method_decorator([login_required], name='dispatch')
class EmpleadoUpdateView(UpdateView):
    model=Empleado
    fields=['nombre', 'empresa', 'tipo_vencimiento', 'fecha', 'segSocial', 'sepe', 'enviadoContrato', 'sage', 'certificadoEmpresa', 'envioLiquidacion', 'firmaFY', 'fin', 'oculto']
    
    success_url="/empleados"

@method_decorator([login_required], name='dispatch')
class EmpleadoDeleteView(DeleteView):
    model=Empleado
    success_url="/empleados"

@method_decorator([login_required], name='dispatch')
class EmpresaCreateView(CreateView):
    model=Empresa
    fields=('nombre', 'asesor')
    success_url="/empleados" 

@method_decorator([login_required], name='dispatch')
class EmpresaUpdateView(UpdateView):
    model=Empresa
    fields=['nombre', 'asesor']
    
    success_url="/listEmpresa"

@method_decorator([login_required], name='dispatch')
class EmpresaListView(ListView):
    model=Empresa

@login_required(login_url='/accounts/login/')
def EmpleadoList(request):
    queryset = request.GET.get("buscar")
    empleados=Empleado.objects.all()
    if queryset:
        empleados = Empleado.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(fecha__icontains = queryset) 
        ).distinct
    hoy=now.date()
        
    return render(request, "nucleo/empleado_list.html", {'empleados':empleados, 'hoy':hoy})