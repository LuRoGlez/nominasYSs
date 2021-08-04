from django.contrib import admin
from nucleo.models import Empresa, Empleado, Asesor, nomYSs, modelo111190, User

from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

# Register your models here.
class EmpresaResource(resources.ModelResource):
    asesor = fields.Field(
        column_name='asesor',
        attribute='asesor',
        widget=ForeignKeyWidget(Asesor, 'nombre')
    )
    class Meta:
        model = Empresa
     
class EmpresaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    resource_class = EmpresaResource

class EmpleadoResource(resources.ModelResource):
    empresa = fields.Field(
        column_name = 'empresa',
        attribute = 'empresa',
        widget=ForeignKeyWidget(Empresa, 'nombre')
    )
    class Meta:
        model = Empleado
        import_id_fields = ('nombre',)
        
class EmpleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'empresa', 'tipo_vencimiento', 'fecha')    
    resource_class = EmpleadoResource

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Asesor)
admin.site.register(nomYSs)
admin.site.register(modelo111190)
admin.site.register(User)