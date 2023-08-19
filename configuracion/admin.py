from django.contrib import admin

from .models import Fraternidad, Medio


class FraternidadAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "mensualidad", "turno_semanal")
    list_display_links = ("id", "nombre")
    # list_editable = ("precio", "nombre")
    search_fields = ("id", "nombre")
    list_per_page = 25


admin.site.register(Fraternidad, FraternidadAdmin)


class MedioAdmin(admin.ModelAdmin):
    list_display = ("id", "image_tag", "tipo", "fraternidad", "upload_date")
    list_display_links = ("id", "fraternidad")
    search_fields = ("id", "descripcion")
    list_filter = ("tipo",)
    list_per_page = 25


admin.site.register(Medio, MedioAdmin)
