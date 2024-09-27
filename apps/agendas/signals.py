from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.agendas.models import Gestion, Mensualidad
from apps.config.models import Fraternidad
import datetime


def get_date(numero_mes, year):
    try:
        return datetime.date(year, numero_mes, 1)
    except ValueError:
        return None


@receiver(post_save, sender=Gestion)
def gestion_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        mensu = 200
        flojonasos = Fraternidad.objects.all().first()
        if flojonasos:
            mensu = flojonasos.mensualidad

        for i in range(1, 13):
            mens = Mensualidad(
                costo=mensu, fecha=get_date(i, instance.anio), mes=i, gestion=instance
            )
            mens.save()
        print("SIGNAL Gestion : Mensualidades creadas")
    else:
        print("SIGNAL Gestion :", "update...")
