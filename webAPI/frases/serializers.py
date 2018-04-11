from rest_framework import serializers
from frases.models import Frase
from django.contrib.auth.models import User


class FraseSerializer(serializers.HyperlinkedModelSerializer):
	owner= serializers.ReadOnlyField(source = 'owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='frase-highlight', format='html')
	class Meta:
		model = Frase
		fields =('url', 'id','highlight', 'owner', 'name', 'release_date', 'rating', 'category')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	frases = serializers.HyperlinkedRelatedField(many=True, view_name='frase-detail', read_only=True)

	class Meta:
		model = User
		fields = ('url', 'id', 'username', 'frases')


