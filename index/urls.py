from django.urls import path
from .views import Personas, Eventos
from . import views

urlpatterns = [
    # path('index/', views.db_evento, name='index'),
    path('accounts/profile/<int:evento_id>/<str:evento_nombre>/', Personas.as_view(), name='db_evento'),
    path('accounts/profile/<int:evento_id>/<str:evento_nombre>/cargaIndividual', views.cargaIndividual, name='cargaIndividual'),
    path('accounts/profile/<int:evento_id>/<str:evento_nombre>/cargaIndividual/<int:persona_id>/', views.cargaIndividual, name='edicion'),
    path('accounts/profile/<int:evento_id>/<str:evento_nombre>/eliminar/<int:persona_id>/', views.Personas.eliminar_persona, name='eliminar_persona'),
    path('accounts/profile/<int:evento_id>/<str:evento_nombre>/cargaMasiva', views.cargaMasiva, name='cargaMasiva'),
    path('index/error.html', views.error_view, name='error'),
    path('eventos/', Eventos.as_view(), name='eventos'),
    ]