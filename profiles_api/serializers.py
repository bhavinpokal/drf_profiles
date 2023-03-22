from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """HelloSerializers class"""
    name = serializers.CharField(max_length=10)
