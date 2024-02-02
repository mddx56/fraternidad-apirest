from csv import DictReader
import csv

from django.core.management import BaseCommand
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from accounts.models import UserAccount


def validate_email_address(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def copy_ci_user(copy):
    try:
        return copy == "Si"
    except TypeError:
        return False


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from children.csv"

    def handle(self, *args, **options):
        print("Cargando....")

        with open("flojonazos.csv", newline="", encoding="utf-8") as File:
            reader = csv.reader(File)
            for row in reader:
                if validate_email_address(row[7]):
                    print(row[7])
                else:
                    print("---")

                user_new = UserAccount(
                    username=row[6],
                    full_name=row[1],
                    ci=row[6],
                    # phone=row[2],
                    email=row[7],
                    # financial_condition=row[4],
                    copy_ci=copy_ci_user(row[4]),
                )
                user_new.set_password("11223344")
                print(user_new)
