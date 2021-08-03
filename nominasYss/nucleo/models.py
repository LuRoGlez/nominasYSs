from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_asesor = models.BooleanField(default=False)

class Asesor(models.Model):
    nombre=models.CharField(max_length=50)
    idUsuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name="asesorA")

    def __str__(self):
        return " Asesor: "+self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    codigo = models.IntegerField(unique=True)
    asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE,related_name="asesorEmp")

    def __str__(self):
        return " Empresa: "+self.nombre

class nomYSs(models.Model):
    nominas = models.BooleanField(default=False)
    rlcRnt = models.BooleanField(default=False)
    cra = models.BooleanField(default=False)
    mes = models.DateField(null=True, blank = True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,related_name="empresaNom")

class modelo111190(models.Model):
    baseIRPF1T = models.FloatField(default=0)
    reten1T = models.FloatField(default=0)
    presentado1T = models.BooleanField(default=False)
    baseIRPF2T = models.FloatField(default=0)
    reten2T = models.FloatField(default=0)
    presentado2T = models.BooleanField(default=False)
    baseIRPF3T = models.FloatField(default=0)
    reten3T = models.FloatField(default=0)
    presentado3T = models.BooleanField(default=False)
    baseIRPF4T = models.FloatField(default=0)
    reten4T = models.FloatField(default=0)
    presentado4T = models.BooleanField(default=False)
    ###bases111 = models.FloatField(null=True, blank=True)
    ###retenciones111= models.FloatField(null=True, blank=True)
    base190 = models.FloatField(default=0)
    reten190 = models.FloatField(default=0)
    ###difBase = models.FloatField(null=True, blank=True)
    ###difReten= models.FloatField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,  related_name="empresa111")

    @property
    def sumaBase(self):
        return (self.baseIRPF1T + self.baseIRPF2T +self.baseIRPF3T + self.baseIRPF4T)

    """def save(self):
        self.bases111 = self.sumaBase
        super(modelo111190, self).save()"""

    @property
    def sumaRetenciones(self):
        retenciones111=(self.reten1T + self.reten2T + self.reten3T + self.reten4T)
        return retenciones111

    """def save(self):
        self.retenciones111 = self.sumaRetenciones
        super(modelo111190, self).save()"""

    @property
    def diferenciaBase(self):
        return ("{0:.2f}".format(self.sumaBase - self.base190))

    """def save(self):
        self.difBase = self.diferenciaBase
        super(modelo111190, self).save()"""

    @property
    def diferenciaRetencion(self):
        return ("{0:.2f}".format(self.sumaRetenciones - self.reten190))

    """def save(self):
        self.difReten = self.diferenciaRetencion
        super(modelo111190, self).save()   """    


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