import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from secret.models import Friends
from django.db.models import Q


#1
class LinkFilter(django_filters.FilterSet):
    class Meta:
        model = Friends
        fields = ['name', 'age']


#2
class LinkNode(DjangoObjectType):
    class Meta:
        model = Friends
        #3
        interfaces = (graphene.relay.Node, )


class RelayQuery(graphene.ObjectType):
    #4
    relay_link = graphene.relay.Node.Field(LinkNode)
    #5
    relay_links = DjangoFilterConnectionField(LinkNode, filterset_class=LinkFilter)