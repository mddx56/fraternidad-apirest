import graphene
from graphene_django import DjangoObjectType

from agendas.models import Agenda, EstadoReserva, TipoEvento

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
            "estado_reserva",
            "user",
            "created_date",
        )


class EstadoReservaType(DjangoObjectType):
    class Meta:
        model = EstadoReserva
        fields = ("id", "nombre")


class TipoEventoType(DjangoObjectType):
    class Meta:
        model = TipoEvento
        fields = ("id", "nombre", "descripcion", "precio")


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Niolia poto ediondo!!")

    all_tipo_eventos = graphene.List(TipoEventoType)
    all_estado_eventos = graphene.List(EstadoReservaType)

    def resolve_all_tipo_eventos(root, info):
        return TipoEvento.objects.all()

    def resolve_all_estado_eventos(root, info):
        return EstadoReserva.objects.all()


schema = graphene.Schema(query=Query)
