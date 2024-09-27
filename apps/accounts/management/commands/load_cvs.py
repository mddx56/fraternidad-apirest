from csv import DictReader
from datetime import datetime
import csv

from django.core.management import BaseCommand
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from accounts.models import UserAccount
from apps.config.models import Cumpleanio


def converter_fecha(fecha):
    try:
        fecha_obj = datetime.strptime(fecha, "%m/%d/%Y")
        fecha_formateada = fecha_obj.strftime("%Y-%m-%d")
        return fecha_formateada
    except ValueError:
        # Manejar el caso en el que la cadena de fecha no es válida
        return None


def validate_email_address(email):
    try:
        validate_email(email)
        return email
    except ValidationError:
        return ""


def copy_ci_user(copy):
    try:
        return copy == "Si"
    except TypeError:
        return False


def state_user(copy):
    if copy == "Activo":
        return "activo"
    else:
        return "suspendido"


def financial_user(option):
    if option == "Normal":
        return "Normal"
    elif option == "Plan de Pagos":
        return "Plan de Pagos"
    else:
        return "Normal"


def supend_user(option):
    if option == "Suspendido":
        return True
    else:
        return False


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from children.csv"

    def handle(self, *args, **options):
        print("Cargando....")

        with open("flojonazos.csv", newline="", encoding="utf-8") as File:
            reader = csv.reader(File)
            for row in reader:
                user_new = UserAccount(
                    username=row[6],
                    full_name=row[1],
                    ci=True,
                    # phone=row[2],
                    email=validate_email_address(row[7]),
                    financial_condition=financial_user(row[3]),
                    copy_ci=copy_ci_user(row[4]),
                    suspend=supend_user(row[2]),
                )
                user_new.set_password("11223344")
                cumple = Cumpleanio(fecha=converter_fecha(row[5]), user=user_new)
                user_new.save()
                cumple.save()
        print("End....")
