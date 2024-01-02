from django.urls import path
from . import views

urlpatterns = [
    # path('index/', views.db_evento, name='index'),
    path('accounts/profile/<int:evento_id>/<str:evento_nombre>/', views.db_evento, name='db_evento'),
    path('accounts/profile/<int:evento_id>/<str:evento_nombre>/cargaIndividual', views.carga_individual, name='cargaIndividual'),
    path('accounts/profile/<int:evento_id>/<str:evento_nombre>/cargaMasiva', views.carga_masiva, name='cargaMasiva'),
    path('index/error.html', views.error_view, name='error'),
    path('eventos/', views.elegirEvento, name='eventos'),
    # path('actualizar_asistencia/', views.actualizar_asistencia, name='actualizar_asistencia'),
    ]