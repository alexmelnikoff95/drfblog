from rest_framework import serializers

from blog.models import Author, Blog, AirBlog


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    text = serializers.CharField()

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class AuthorSr(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance


class AirBlogSerializer(serializers.Serializer):
    title = serializers.CharField()
    text = serializers.CharField()

    def create(self, validated_data):
        return AirBlog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
