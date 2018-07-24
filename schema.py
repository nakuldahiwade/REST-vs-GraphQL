import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import *


class Compute(SQLAlchemyObjectType):

    class Meta:
        model = Compute
        interfaces = (relay.Node, )


class Network(SQLAlchemyObjectType):

    class Meta:
        model = Network
        interfaces = (relay.Node, )


class Volume(SQLAlchemyObjectType):
    class Meta:
        model = Volume
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):

    node = relay.Node.Field()
    all_vms = SQLAlchemyConnectionField(Compute)


schema = graphene.Schema(query=Query)