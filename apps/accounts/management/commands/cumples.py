import csv
from datetime import datetime
from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from apps.config.models import Cumpleanio


def converter_fecha(fecha):
    try:
        fecha_obj = datetime.strptime(fecha, "%m/%d/%Y")
        fecha_formateada = fecha_obj.strftime("%Y-%m-%d")
        return fecha_formateada
    except ValueError:
        return None


User = get_user_model()


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from children.csv"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Cargando...."))
        with open("cumples.csv", newline="", encoding="utf-8") as File:
            reader = csv.reader(File)
            for row in reader:
                user_c = User.objects.all()
                cii = row[1]
                for ss in user_c:
                    if ss.username == cii.strip():
                        # print(converter_fecha(row[0].strip()))
                        cumple = Cumpleanio(
                            fecha=converter_fecha(row[0].strip()), user=ss
                        )
                        cumple.save()
        self.stdout.write(self.style.SUCCESS("cumpleaños agregados!!"))
