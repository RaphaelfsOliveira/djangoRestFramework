# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),

    url(r'^v1/snippets/$', views.snippet_list),
    url(r'^v1/snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

    # usando class-based views
    url(r'^v2/snippets/$', views.SnippetList.as_view()),
    url(r'^v2/snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),

    # Usando Mixins Class-based views
    url(r'^v3/snippets/$', views.SnippetListMix.as_view()),
    url(r'^v3/snippets/(?P<pk>[0-9]+)/$', views.SnippetDetailMix.as_view()),

    # Usando Generic Class-based views
    url(r'^snippets/$', views.SnippetListGeneric.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetailGeneric.as_view(), name='snippet-detail'),

    url(r'^users/$', views.UserList.as_view(), name='users-list'),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name='users-detail'),

    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]
