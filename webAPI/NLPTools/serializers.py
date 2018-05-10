from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk','writter','text','token')
    
    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Post` instance, given the validated data.
        """
        instance.pk = validated_data.get('pk', instance.pk)
        instance.writter = validated_data.get('writter', instance.writter)
        instance.text = validated_data.get('text', instance.text)
        instance.token = validated_data.get('token', instance.token)
        instance.save()
        return instance