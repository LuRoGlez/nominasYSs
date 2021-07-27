"""nominasYss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from nucleo import views

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

   
]
