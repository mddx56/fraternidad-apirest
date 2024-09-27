from django.core.management import BaseCommand
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

fraternos = Q(role="Fraterno") | Q(role="Tesorero")


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_LABEL("Cargando...."))
        new_password = "11223344"
        User = get_user_model()
        fraters = User.objects.filter(fraternos).order_by("full_name")

        for user in fraters:
            print(user.full_name)
            user.password = make_password(new_password)
            user.save()

        self.stdout.write(self.style.SUCCESS("Contraseñas actualizadas!!"))
