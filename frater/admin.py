from django.contrib import admin

from .models import (
    Fraternidad,
    Cumpleanio,
)

admin.site.register(Fraternidad)
admin.site.register(Cumpleanio)
