from django.contrib import admin

from .models import (
    Fraternidad,
    MediaImage,
    MediaVideo,
    Articulo,
    Cumpleanio,
    Horario,
    Actividad,
    DiaSemana,
    Cronograma,
)


class CumpleanioAdmin(admin.ModelAdmin):
    list_display = ("fecha", "disponible", "user")
    list_display_links = ("fecha", "disponible")
    list_per_page = 25


admin.site.register(Cumpleanio, CumpleanioAdmin)


class FraternidadAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "mensualidad", "turno_semanal")
    list_display_links = ("id", "nombre")
    # list_editable = ("precio", "nombre")
    search_fields = ("id", "nombre")
    list_per_page = 25


admin.site.register(Fraternidad, FraternidadAdmin)


class MediaImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image_tag", "secuencia", "mostrar", "upload_date")
    list_display_links = ("id",)
    search_fields = ("id", "descripcion")
    list_filter = ("mostrar",)
    list_editable = ("mostrar", "secuencia")
    ordering = ["secuencia"]
    list_per_page = 25


admin.site.register(MediaImage, MediaImageAdmin)


class MediaVideoAdmin(admin.ModelAdmin):
    list_display = ("id", "video_tag", "video_id", "descripcion", "upload_date")
    list_display_links = ("id",)
    search_fields = ("id", "video_id", "descripcion")
    list_filter = ("mostrar",)
    ordering = ["id"]
    list_per_page = 25


admin.site.register(MediaVideo, MediaVideoAdmin)


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "mostrar", "upload_date")
    list_display_links = ("id", "titulo")
    search_fields = ("id", "titulo")
    list_filter = ("mostrar",)
    ordering = ["id"]
    list_per_page = 25


admin.site.register(Horario)

admin.site.register(Actividad)
admin.site.register(DiaSemana)
admin.site.register(Cronograma)
