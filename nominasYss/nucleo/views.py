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
        empleados = Empleado.objects.filter(oculto = False).filter(
            Q(nombre__icontains = queryset) |
            Q(fecha__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct
    hoy=now.date()
    empl = Empleado.objects.filter(fin=False, fecha__lte=hoy)
    for em in empl:
        messages.info(request, 'ATENCIÓN '+em.empresa.asesor.nombre+'! El trabajador '+em.nombre+' ha vencido la fecha establecida')
        
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
            Q(fecha__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct
    hoy=now.date()
        
    return render(request, "nucleo/empleado_list.html", {'empleados':empleados, 'hoy':hoy})


@login_required(login_url='/accounts/login/')
def Modelo111190(request):
    queryset = request.GET.get("buscar")
    modelo111=modelo111190.objects.filter(oculto = False)
    if queryset:
        modelo111 = modelo111190.objects.filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct
    
            
    return render(request, "nucleo/modelo111190.html", {'modelo111':modelo111})

@method_decorator([login_required], name='dispatch')
class modelo111190UpdateView(UpdateView):
    model=modelo111190
    fields=['baseIRPF1T', 'reten1T', 'presentado1T', 'baseIRPF2T', 'reten2T', 'presentado2T', 'baseIRPF3T', 'reten3T', 'presentado3T', 'baseIRPF4T', 'reten4T', 'presentado4T','base190', 'reten190', 'anyo','fin', 'oculto']
    
    success_url="/modelo111190"

@method_decorator([login_required], name='dispatch')
class modelo111190DeleteView(DeleteView):
    model=modelo111190
    success_url="/modelo111190"

@login_required(login_url='/accounts/login/')
def Nominas(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False)
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/nominas.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})


@method_decorator([login_required], name='dispatch')
class modelo111190CreateView(CreateView):
    model = modelo111190
    fields=('empresa', 'anyo')
    success_url="/modelo111190"

def Modelo111190Historial(request):
    queryset = request.GET.get("buscar")
    modelo111=modelo111190.objects.all()
    if queryset:
        modelo111 = modelo111190.objects.filter(
            Q(anyo__icontains = queryset) 
        ).distinct
    
            
    return render(request, "nucleo/modelo111190Historial.html", {'modelo111':modelo111})

@login_required(login_url='/accounts/login/')
def NominasHistorial(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.all()
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(
            Q(anyo__icontains = queryset) |
            Q(mes__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count() 
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/nominasHistorial.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})


@login_required(login_url='/accounts/login/')
def Ene(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False).filter(mes = 'Enero')
    
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(mes='Enero').filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/ene.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})

@login_required(login_url='/accounts/login/')
def Feb(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False).filter(mes = 'Febrero')
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(mes='Febrero').filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/feb.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})

@login_required(login_url='/accounts/login/')
def Mar(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False).filter(mes = 'Marzo')
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(mes='Marzo').filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/mar.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})

@login_required(login_url='/accounts/login/')
def Abr(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False).filter(mes = 'Abril')
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(mes='Abril').filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/abr.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})

@login_required(login_url='/accounts/login/')
def May(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False).filter(mes = 'Mayo')
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(mes='Mayo').filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/may.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})

@login_required(login_url='/accounts/login/')
def Jun(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False).filter(mes = 'Junio')
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(mes='Junio').filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/jun.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})

@login_required(login_url='/accounts/login/')
def Jul(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False).filter(mes = 'Julio')
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(mes='Julio').filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/jul.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})


@login_required(login_url='/accounts/login/')
def Ago(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False).filter(mes = 'Agosto')
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(mes='Agosto').filter(            
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/ago.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})

@login_required(login_url='/accounts/login/')
def Sep(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False).filter(mes = 'Septiembre')
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(mes='Septiembre').filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/sep.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})

@login_required(login_url='/accounts/login/')
def Oct(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False).filter(mes = 'Octubre')
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(mes='Octubre').filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/oct.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})

@login_required(login_url='/accounts/login/')
def Nov(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False).filter(mes = 'Noviembre')
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(mes='Noviembre').filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/nov.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})

@login_required(login_url='/accounts/login/')
def Dic(request):
    empresas=Empresa.objects.all()
    nominas= nomYSs.objects.filter(oculto = False).filter(mes = 'Diciembre')
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        nominas = nomYSs.objects.filter(oculto = False).filter(mes='Diciembre').filter(
            Q(anyo__icontains = queryset) |
            Q(empresa__asesor__nombre__icontains = queryset) |
            Q(empresa__nombre__icontains = queryset)
        ).distinct


    emElena= Empresa.objects.filter(asesor = 1).count()
    emMaria= Empresa.objects.filter(asesor = 3).count()
    emCarmen= Empresa.objects.filter(asesor = 2).count()
    emSara= Empresa.objects.filter(asesor = 5).count()
    emJoseLuis= Empresa.objects.filter(asesor = 4).count()


    return render(request, "nucleo/dic.html", {'empresas':empresas, 'nominas':nominas, 'emElena':emElena, 'emMaria':emMaria, 'emSara':emSara, 'emCarmen':emCarmen, 'emJoseLuis':emJoseLuis})

@method_decorator([login_required], name='dispatch')
class nomYSsUpdateView(UpdateView):
    model=nomYSs
    fields=['nominas', 'rlcRnt', 'cra', 'anyo', 'mes', 'fin', 'oculto']
    
    success_url="/nominas"

@method_decorator([login_required], name='dispatch')
class nomYSsDeleteView(DeleteView):
    model=nomYSs
    success_url="/nominas"

@method_decorator([login_required], name='dispatch')
class nomYSsCreateView(CreateView):
    model = nomYSs
    fields=('empresa', 'anyo', 'mes')
    success_url="/nominas"