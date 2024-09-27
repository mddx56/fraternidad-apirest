from django.apps import AppConfig


class AgendasConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.agendas"
    verbose_name = "Administrar Agenda"

    def ready(self):
        import apps.agendas.signals
