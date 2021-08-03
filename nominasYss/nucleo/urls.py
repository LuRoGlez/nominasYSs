
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
    path('listModelo111190',views.modelo111190ListView.as_view(), name="listModelo111190"),
    path('updateModelo111190/<int:pk>',views.modelo111190UpdateView.as_view(), name="updateModelo111190"),

   
]