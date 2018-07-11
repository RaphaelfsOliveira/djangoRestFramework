# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework import renderers
from snippets import views
from snippets.views import SnippetViewSet, UserViewSet


# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# agora eu crio um router e registro a viewset nele
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# format_suffix_patterns o router tambem gera automaticamente, tirei do código aqui
urlpatterns = [
    # usando viewsets e routers a url é gerada automaticamente
    url(r'^', include(router.urls)),

    # DefaultRouter cria automaticamente a api_root logo não precisamos mais definir
    # url(r'^$', views.api_root),

    # # usando Viewsets
    # url(r'^snippets/$', snippet_list, name='snippet-list'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    #
    # url(r'^users/$', user_list, name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)$', user_detail, name='user-detail'),
    #
    # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),

    # # usando Function-based views
    # url(r'^v1/snippets/$', views.snippet_list),
    # url(r'^v1/snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    #
    # # usando class-based views
    # url(r'^v2/snippets/$', views.SnippetList.as_view()),
    # url(r'^v2/snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    #
    # # Usando Mixins Class-based views
    # url(r'^v3/snippets/$', views.SnippetListMix.as_view()),
    # url(r'^v3/snippets/(?P<pk>[0-9]+)/$', views.SnippetDetailMix.as_view()),
    #
    # # Usando Generic Class-based views
    # url(r'^v5/snippets/$', views.SnippetListGeneric.as_view(), name='snippet-list'),
    # url(r'^v5/snippets/(?P<pk>[0-9]+)/$', views.SnippetDetailGeneric.as_view(), name='snippet-detail'),
    #
    # url(r'^v5/users/$', views.UserList.as_view(), name='users-list'),
    # url(r'^v5/users/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name='users-detail'),
    #
    # url(r'^v5/snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]
