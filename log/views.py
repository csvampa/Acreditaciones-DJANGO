from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from index.models import Evento


def profiles(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect ('eventos')
        else:
            user=request.user
            evento = Evento.objects.get(auth_user=user)
            return redirect('db_evento', evento_id=evento.id, evento_nombre=evento.nombre)
    else:
         return LoginView.as_view()(request)