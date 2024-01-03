from django.urls import path
from . import views

urlpatterns = [
    # path('index/', views.db_evento, name='index'),
    path('accounts/profile/<int:evento_id>/<str:evento_nombre>/', views.db_evento.Personas, name='db_evento'),
    path('accounts/profile/<int:evento_id>/<str:evento_nombre>/cargaIndividual', views.carga_individual.Personas, name='cargaIndividual'),
    path('accounts/profile/<int:evento_id>/<str:evento_nombre>/cargaMasiva', views.carga_masiva.Personas, name='cargaMasiva'),
    path('index/error.html', views.error_view, name='error'),
    path('eventos/', views.elegirEvento.Personas, name='eventos'),
    # path('actualizar_asistencia/', views.actualizar_asistencia, name='actualizar_asistencia'),
    ]