import graphene

from graphene_django.types import DjangoObjectType

from .models import *


class ChampionType(DjangoObjectType):
    class Meta:
        model = Champion

class MapType(DjangoObjectType):
    class Meta:
        model = Map



class Query(object):
    all_champions = graphene.List(ChampionType)
    all_maps = graphene.List(MapType)

    def resolve_all_champions(self, info, **kwargs):
        return Champion.objects.all().order_by('role', 'name')

    def resolve_all_maps(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Map.objects.all().order_by('name')
