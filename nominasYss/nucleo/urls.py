
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('listEmpleado',views.EmpleadoList, name="listEmpleado"),
    path('createEmpleado',views.EmpleadoCreateView.as_view(), name="createEmpleado"),
    path('updateEmpleado/<int:pk>',views.EmpleadoUpdateView.as_view(), name="updateEmpleado"),
    path('deleteEmpleado/<int:pk>',views.EmpleadoDeleteView.as_view(), name="deleteEmpleado"),
    path('createEmpresa',views.EmpresaCreateView.as_view(), name="createEmpresa"),
    path('updateEmpresa/<int:pk>',views.EmpresaUpdateView.as_view(), name="updateEmpresa"),
    path('listEmpresa',views.EmpresaListView.as_view(), name="listEmpresa"),
    path('empleados',views.Empleados, name="empleados"),
    path('updateModelo111190/<int:pk>',views.modelo111190UpdateView.as_view(), name="updateModelo111190"),
    path('deleteModelo111190/<int:pk>',views.modelo111190DeleteView.as_view(), name="deleteModelo111190"),
    path('nominas',views.Nominas, name="nominas"),
    path('modelo111190',views.Modelo111190, name="modelo111190"),
    path('createModelo111190',views.modelo111190CreateView.as_view(), name="createModelo111190"),
    path('modelo111190Historial',views.Modelo111190Historial, name="modelo111190Historial"),
    path('nominasHistorial',views.NominasHistorial, name="nominasHistorial"),
    path('ene',views.Ene, name="ene"),
    path('feb',views.Feb, name="feb"),
    path('mar',views.Mar, name="mar"),
    path('abr',views.Abr, name="abr"),
    path('may',views.May, name="may"),
    path('jun',views.Jun, name="jun"),
    path('jul',views.Jul, name="jul"),
    path('ago',views.Ago, name="ago"),
    path('sep',views.Sep, name="sep"),
    path('oct',views.Oct, name="oct"),
    path('nov',views.Nov, name="nov"),
    path('dic',views.Dic, name="dic"),
    path('updatenomYSs/<int:pk>',views.nomYSsUpdateView.as_view(), name="updatenomYSs"),
    path('deletenomYSs/<int:pk>',views.nomYSsDeleteView.as_view(), name="deletenomYSs"),
    path('createnomYSs',views.nomYSsCreateView.as_view(), name="createnomYSs"),
]