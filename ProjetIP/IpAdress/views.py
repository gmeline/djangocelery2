
from django.shortcuts import redirect
from  django.views.generic import TemplateView

from .models import Server, Command,IP
from rest_framework import viewsets
from .serializers import ServerSerializer

class IndexView (TemplateView):
    model= Server
    template_name='index.html'
    context_object_name='server'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['liste_server'] = Server.objects.all()
        context['liste_command'] = Command.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        ip_address = request.POST.get('ip_address')
        if ip_address:
            new_ip = IP.objects.create(number=ip_address)
            return redirect('index')
        return super().get(request, *args, **kwargs)

class ServerViewSet(viewsets.ModelViewSet):
    serializer_class = ServerSerializer
    queryset = Server.objects.all()
