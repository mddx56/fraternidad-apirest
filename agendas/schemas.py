import graphene
from graphene_django import DjangoObjectType

from agendas.models import Agenda, Qr, TipoEvento

# from models.


class EventoType(DjangoObjectType):
    class Meta:
        model = Agenda
        fields = (
            "id",
            "fecha",
            "hora_inicio",
            "hora_fin",
            "descripcion",
            "tipo_evento",
            "es_entresemana",
            "estado_reserva",
            "user",
            "created_date",
        )


class TipoEventoType(DjangoObjectType):
    class Meta:
        model = TipoEvento
        fields = ("id", "nombre", "descripcion", "costo_entresemana", "costo_finsemana")


class QrType(DjangoObjectType):
    class Meta:
        model = Qr
        fields = ("id", "qr_valor", "url", "descripcion", "tipo_evento")


class Query(graphene.ObjectType):

    all_eventos = graphene.List(EventoType)
    count_eventos = graphene.Int()

    all_tipo_eventos = graphene.List(TipoEventoType)
    all_qrs = graphene.List(QrType)

    def resolve_count_eventos(root, info) -> int:
        return Agenda.objects.all().count()

    def resolve_all_eventos(root, info):
        return Agenda.objects.all()

    def resolve_all_tipo_eventos(root, info):
        return TipoEvento.objects.all()

    def resolve_all_qrs(root, info):
        return Qr.objects.all()


schema = graphene.Schema(query=Query)
