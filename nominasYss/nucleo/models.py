from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_asesor = models.BooleanField(default=False)

class Asesor(models.Model):
    nombre=models.CharField(max_length=50)
    idUsuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name="asesorA")

class Empresa(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    codigo = models.IntegerField(unique=True)
    asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE,related_name="asesorEmp")

class nomYSs(models.Model):
    nominas = models.BooleanField(default=False)
    rlcRnt = models.BooleanField(default=False)
    cra = models.BooleanField(default=False)
    mes = models.DateField(null=True, blank = True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,related_name="empresaNom")

class modelo111190(models.Model):
    baseIRPF = models.FloatField()
    rent = models.FloatField()
    presentado = models.BooleanField(default=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,  related_name="empresa111")


class Empleado (models.Model):
    nombre = models.CharField(max_length=100)
    empresa=models.ForeignKey(Empresa, verbose_name="Empresa", on_delete=models.CASCADE, related_name='empresaEmp')

    class Vencimientos(models.TextChoices):
        ALTA = 'ALTA'
        BAJA = 'BAJA'
        BAJA51 = 'BAJA 51'
        BAJA93 = 'BAJA 93'
        BAJA85= 'BAJA 85'
        BAJA91 = 'BAJA 91'
        BAJA53 = 'BAJA 53'
        BAJA94 = 'BAJA 94'
        BAJA54 = 'BAJA 54'
        REDUCCION_JORNADA = 'REDUCCIÓN DE JORNADA'
        AMPLIACION_JORNADA = 'AMPLIACIÓN DE JORNADA'
        INACTIVIDAD = 'INACTIVIDAD'
        TRANSFORMACION = 'TRANSFORMACIÓN'
        PRORROGA = 'PROROGA'
        DESAFECTACION = 'DESAFECTACIÓN'
        LLAMAMIENTO = 'LLAMAMIENTO'
        BAJA_Y_ALTA = 'BAJA Y ALTA' 
   
    tipo_vencimiento = models.CharField(max_length=25, choices=Vencimientos.choices, blank=True, default='BAJA')
    fecha=models.DateField(null=True, blank = True)
    segSocial=models.BooleanField(default=False)
    sepe=models.BooleanField(default=False)
    enviadoContrato=models.BooleanField(default=False)
    sage=models.BooleanField(default=False)
    certificadoEmpresa=models.BooleanField(default=False)
    envioLiquidacion=models.BooleanField(default=False)
    firmaFY=models.BooleanField(default=False)
    fin=models.BooleanField(default=False)
    oculto=models.BooleanField(default=False)

    class Meta:
        ordering = ['fecha']
    

    def __str__(self):
        return " Empleado: "+self.nombre+" Empresa: "+self.empresa.nombre+" Tipo Vencimiento: "+self.tipo_vencimiento