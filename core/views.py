from django.shortcuts import render, redirect
from agendas.models import TipoEvento
from configuracion.models import Fraternidad, MediaImage
from django.http import Http404


def index(request):
    return redirect("/home")


def home(request):
    frater = Fraternidad.objects.all().first()
    fotos = MediaImage.objects.all()
    events = TipoEvento.objects.all()
    template = "index.html"
    return render(
        request, template, {"frater": frater, "fotos": fotos, "events": events}
    )
