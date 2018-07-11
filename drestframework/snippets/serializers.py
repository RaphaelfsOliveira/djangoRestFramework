# -*- coding: utf-8 -*-
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    owner_id = serializers.ReadOnlyField(source='owner.id')

    highlight = serializers.HyperlinkedIdentityField(view_name='snippets:snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'title', 'owner_id',
                  'owner', 'code', 'linenos', 'language', 'style')
        extra_kwargs = {
            'url': {'view_name': 'snippets:snippet-detail'},
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippets:snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
        extra_kwargs = {
            'url': {'view_name': 'snippets:user-detail'}
        }
