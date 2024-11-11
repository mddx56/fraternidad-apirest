from django.shortcuts import render, redirect
from apps.agendas.models import TipoEvento
from apps.config.models import Fraternidad, MediaImage
from django.http import Http404


def index(request):
    return redirect("/home")


def privacy(request):
    frater = Fraternidad.objects.all().first()
    template = "privacy.html"
    return render(request, template, {"frater": frater})


def home(request):
    frater = Fraternidad.objects.all().first()
    # fotos = MediaImage.objects.all()
    events = TipoEvento.objects.all()
    template = "index.html"
    return render(request, template, {"frater": frater, "events": events})
