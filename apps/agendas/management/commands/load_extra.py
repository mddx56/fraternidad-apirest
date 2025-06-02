from csv import DictReader

# from datetime import datetime
import csv
import datetime

from django.core.management import BaseCommand
from apps.accounts.models import UserAccount
from apps.agendas.models import DetallePagoExtraordianria


def limpiarPagos():
    try:
        DetallePagoExtraordianria.objects.all().delete()
    except TypeError as e:
        print(f"Error: Tipo de dato incorrecto - {e}")
    finally:
        print("se limpio los datos correctamente")


def detectar_repetidos(array):
    elementos_repetidos = []
    for elemento in array:
        if array.count(elemento) > 1 and elemento not in elementos_repetidos:
            elementos_repetidos.append(elemento)
    return elementos_repetidos


class Command(BaseCommand):
    help = "Loads data from extraord.csv"

    def handle(self, *args, **options):
        print("Cargando pagos extraordinarias....")
        limpiarPagos()

        with open("extraord.csv", newline="", encoding="utf-8") as File:
            reader2 = csv.reader(File)
            for row2 in reader2:
                for ele in row2:
                    self.stdout.write(self.style.SUCCESS(ele))
                self.stdout.write(self.style.MIGRATE_LABEL("**********"))
        print("Fin....")
