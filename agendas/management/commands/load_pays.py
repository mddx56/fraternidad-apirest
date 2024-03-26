from csv import DictReader

# from datetime import datetime
import csv
import datetime

from django.core.management import BaseCommand
from accounts.models import UserAccount
from agendas.models import Mensualidad, DetallePagoMensualidad, Gestion, Pago


def detectar_repetidos(array):
    elementos_repetidos = []
    for elemento in array:
        if array.count(elemento) > 1 and elemento not in elementos_repetidos:
            elementos_repetidos.append(elemento)
    return elementos_repetidos


def create_gestion():
    gestion_23 = Gestion.objects.filter(anio=2023)
    gestion_24 = Gestion.objects.filter(anio=2024)
    if not gestion_23.exists():
        gestion23 = Gestion(anio=2023, en_curso=False)
        gestion23.save()
        print("gestion 2023 creada")
    else:
        print("gestion 2023 ya existe")
    if not gestion_24.exists():
        gestion24 = Gestion(anio=2024, en_curso=True)
        gestion24.save()
        print("gestion 2024 creada")
    else:
        print("gestion 2024 ya existe")


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pays.csv"

    def handle(self, *args, **options):
        print("Cargando pagos....")
        datos_meses = {
            0: {"mes": 1, "anio": 2023},
            1: {"mes": 2, "anio": 2023},
            2: {"mes": 3, "anio": 2023},
            3: {"mes": 4, "anio": 2023},
            4: {"mes": 5, "anio": 2023},
            5: {"mes": 6, "anio": 2023},
            6: {"mes": 7, "anio": 2023},
            7: {"mes": 8, "anio": 2023},
            8: {"mes": 9, "anio": 2023},
            9: {"mes": 10, "anio": 2023},
            10: {"mes": 11, "anio": 2023},
            11: {"mes": 12, "anio": 2023},
            12: {"mes": 1, "anio": 2024},
            13: {"mes": 2, "anio": 2024},
            14: {"mes": 3, "anio": 2024},
            15: {"mes": 4, "anio": 2024},
            16: {"mes": 5, "anio": 2024},
            17: {"mes": 6, "anio": 2024},
            18: {"mes": 7, "anio": 2024},
            19: {"mes": 8, "anio": 2024},
            20: {"mes": 9, "anio": 2024},
            21: {"mes": 10, "anio": 2024},
            22: {"mes": 11, "anio": 2024},
            23: {"mes": 12, "anio": 2024},
        }
        
        create_gestion()

        with open("pays.csv", newline="", encoding="utf-8") as File:

            reader2 = csv.reader(File)
            index = 0
            switch = False
            for row2 in reader2:
                index = 0
                switch = False
                for ele in row2:
                    if len(ele.strip()) > 3 and not switch:
                        ci = ele.strip()
                        user_frater = UserAccount.objects.filter(username=ci).first()
                       
                        print("CI :", user_frater.username)
                        switch = True
                    elif ele.strip() == "200" and switch:
                        mes_pago = datos_meses[index - 1]["mes"]
                        anio_pago = datos_meses[index - 1]["anio"]
                        gestion_pago=Gestion.objects.filter(anio=anio_pago).first()
                        mensualidad_pago=Mensualidad.objects.filter(mes=mes_pago,gestion=gestion_pago).first()
                        pago_pago = Pago(
                            fecha_pago=datetime.datetime.now(),
                            monto_pagado=mensualidad_pago.costo,
                            user=user_frater,
                        )
                        pago_pago.save()
                        detalle=DetallePagoMensualidad(pago = pago_pago,mensualidad=mensualidad_pago)
                        detalle.save()
                        print(detalle)
                        print(mensualidad_pago)
                        #print("pagado ", f"{mes}, {anio}")
                    else:
                        mes = datos_meses[index - 1]["mes"]
                        anio = datos_meses[index - 1]["anio"]
                        print("No pagado ", f"{mes}, {anio}")
                    index = index + 1
        print("Fin....")
