# coding=utf-8
from __future__ import unicode_literals


from django.conf.urls import include, url
from graphene_django.views import GraphQLView


urlpatterns = [
    
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    
]
