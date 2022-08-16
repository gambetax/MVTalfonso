from django.urls import path
from AppMVTalfonso.views import inicio,familia,familias,consultar_familia
from AppMVTalfonso.views import integrante,integrantes

urlpatterns = [
    path('',inicio,name='AppMVTalfonsoInicio'),
    path('familia/<apellido>/<cantidad_integrantes>',familia,name='AppMVTalfonsoFamilia'),
    path('familias',familias,name='AppMVTalfonsoFamilias'),
    path('consultarFamilia/<apellido>',consultar_familia),
    path('integrante/<nombre>/<apellido>/<edad>',integrante),
    path('integrantes',integrantes),
    path('integrantes/apellido',integrantes),
]