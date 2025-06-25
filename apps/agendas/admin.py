from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
from admin_interface.admin import Theme
from django.urls import path
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Pago, DetallePagoMensualidad, Mensualidad, User
from django.db.models import Sum
from django.contrib.admin import AdminSite

admin.site.unregister(Group)
admin.site.unregister(Theme)

from .models import (
    Agenda,
    Pago,
    TipoEvento,
    Gestion,
    Qr,
    Turno,
    UserTurno,
    Mensualidad,
    Extraordinaria,
    DetallePagoEvento,
    DetallePagoExtraordianria,
    DetallePagoMensualidad,
    GrupoTurno,
    Cupon,
    # Cuota,
    # DetallePagoExtraord,
    # FraterExtraord,
)

admin.site.site_header = "Sistema de Gestión para Fraternidad ⛺"
admin.site.site_title = "Flojonazos"
admin.site.index_title = "Bienvenidos al portal de administración"

"""
admin.site.register(Extraord)
admin.site.register(Cuota)
admin.site.register(DetallePagoExtraord)
admin.site.register(FraterExtraord)
"""


class GestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "anio",
        "en_curso",
    )
    list_display_links = ("id", "anio")
    # list_editable = ("precio", "nombre")
    search_fields = ("id", "anio")
    list_per_page = 25


admin.site.register(Gestion, GestionAdmin)


class QrAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "qr_valor",
        "url",
        "descripcion",
        "tipo_evento",
    )
    list_display_links = (
        "id",
        "qr_valor",
    )
    # list_editable = ("precio", "nombre")
    search_fields = ("id", "descripcion")
    list_per_page = 25


# admin.site.register(Qr, ImportExportModelAdmin)
admin.site.register(Qr, QrAdmin)


class TurnoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fecha",
        "grupo_turno",
    )
    list_display_links = (
        "id",
        "fecha",
    )
    list_filter = (
        "grupo_turno",
        "fecha",
    )
    # list_editable = ("precio", "nombre")
    search_fields = ("id", "fecha")
    list_per_page = 25


admin.site.register(Turno, TurnoAdmin)


class DetallePagoEventoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pago",
        "evento",
    )
    list_display_links = (
        "id",
        "pago",
    )
    search_fields = ("id", "pago")
    list_per_page = 25


admin.site.register(DetallePagoEvento, DetallePagoEventoAdmin)


class DetallePagoExtraordianriaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pago",
        # "deuda_extraordinaria",
    )
    list_display_links = (
        "id",
        "pago",
    )

    # list_editable = ("precio", "nombre")
    search_fields = ("id", "pago")
    list_per_page = 25


admin.site.register(DetallePagoExtraordianria, DetallePagoExtraordianriaAdmin)


"""class DetallePagoMensualidadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pago",
        "mensualidad",
    )
    list_display_links = (
        "id",
        "pago",
    )

    # list_editable = ("precio", "nombre")
    search_fields = ("id", "pago")
    list_per_page = 25


admin.site.register(DetallePagoMensualidad, DetallePagoMensualidadAdmin)"""


class TipoEventoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "descripcion",
        "costo_entresemana",
        "costo_finsemana",
    )
    list_display_links = (
        "id",
        "nombre",
    )
    # list_editable = ("precio", "nombre")
    search_fields = ("id", "nombre")
    list_per_page = 25


admin.site.register(TipoEvento, TipoEventoAdmin)


class AgendaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fecha",
        "descripcion",
        "es_entresemana",
        "tipo_evento",
        "user",
    )
    list_display_links = (
        "id",
        "user",
        "fecha",
    )
    list_filter = ("tipo_evento",)
    search_fields = ("id", "user")


admin.site.register(Agenda, AgendaAdmin)


"""class PagoAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha_pago", "monto_pagado", "user", "created_date")
    list_display_links = ("id", "user")
    list_filter = ("fecha_pago",)
    search_fields = ("id", "user")


admin.site.register(Pago, PagoAdmin)"""


class GrupoTurnoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "dia")
    list_display_links = ("id", "nombre")
    list_filter = ("nombre",)
    list_per_page = 25


admin.site.register(GrupoTurno, GrupoTurnoAdmin)


class UserTurnoAdmin(admin.ModelAdmin):
    list_display = ("id", "grupo_turno", "user")
    list_display_links = ("id", "grupo_turno", "user")
    list_per_page = 25


admin.site.register(UserTurno, UserTurnoAdmin)


class MensualidadAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha", "costo", "gestion")
    list_display_links = ("id", "fecha")
    # list_filter = ( "gestion")
    search_fields = ("fecha",)
    list_per_page = 25


admin.site.register(Mensualidad, MensualidadAdmin)


class ExtraordinariaAdmin(admin.ModelAdmin):
    list_display = (
        "monto",
        "concepto",
        "created_date",
    )


admin.site.register(Extraordinaria, ExtraordinariaAdmin)


class CuponAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fecha",
        "estado",
        "user",
    )


admin.site.register(Cupon, CuponAdmin)


class DetallePagoMensualidadInline(admin.TabularInline):
    model = DetallePagoMensualidad
    extra = 1


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ["user", "fecha_pago", "monto_pagado"]


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    form = PagoForm
    list_display = ("id", "user", "fecha_pago", "monto_pagado", "created_date")
    list_filter = ("fecha_pago", "user")
    search_fields = ("user__username",)
    inlines = [DetallePagoMensualidadInline]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "registrar-pago/",
                self.admin_site.admin_view(self.registrar_pago_view),
                name="registrar_pago",
            ),
            path(
                "reporte-pagos/",
                self.admin_site.admin_view(self.reporte_pagos_view),
                name="reporte_pagos",
            ),
        ]
        return custom_urls + urls

    def registrar_pago_view(self, request):
        if request.method == "POST":
            form = PagoForm(request.POST)
            if form.is_valid():
                pago = form.save()
                mensualidades_ids = request.POST.getlist("mensualidades")
                for mensualidad_id in mensualidades_ids:
                    DetallePagoMensualidad.objects.create(
                        pago=pago, mensualidad_id=mensualidad_id
                    )
                messages.success(request, "Pago registrado exitosamente!")
                return redirect("admin:pagos_pago_changelist")
        else:
            form = PagoForm()

        # Obtener mensualidades pendientes
        mensualidades_pendientes = Mensualidad.objects.filter(
            pagada=False
        ).select_related("user")

        context = dict(
            self.admin_site.each_context(request),
            title="Registrar Nuevo Pago",
            form=form,
            mensualidades_pendientes=mensualidades_pendientes,
        )
        return render(request, "admin/pagos/registrar_pago.html", context)

    def reporte_pagos_view(self, request):
        pagos_por_usuario = (
            Pago.objects.values("user__username")
            .annotate(total_pagado=Sum("monto_pagado"))
            .order_by("user__username")
        )

        total_general = Pago.objects.aggregate(total=Sum("monto_pagado"))["total"] or 0

        context = dict(
            self.admin_site.each_context(request),
            title="Reporte de Pagos",
            pagos_por_usuario=pagos_por_usuario,
            total_general=total_general,
        )
        return render(request, "admin/pagos/reporte_pagos.html", context)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["opts"] = self.model._meta
        return super().changelist_view(request, extra_context=extra_context)


class CustomAdminSite(AdminSite):
    def get_app_list(self, request):
        app_list = super().get_app_list(request)

        app_list.append(
            {
                "name": "Pagos New",
                "app_label": "pagos_custom",
                "models": [
                    {
                        "name": "Registrar Pago",
                        "object_name": "registrar_pago",
                        "admin_url": "/admin/pagos/pago/registrar-pago/",
                        "view_only": True,
                    },
                    {
                        "name": "Reporte de Pagos",
                        "object_name": "reporte_pagos",
                        "admin_url": "/admin/pagos/pago/reporte-pagos/",
                        "view_only": True,
                    },
                ],
            }
        )

        return app_list


admin_site = CustomAdminSite(name="myadmin")
