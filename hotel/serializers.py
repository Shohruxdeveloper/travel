from rest_framework import serializers
from .models import Travel, Hotel, Klass


class TravelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    comment = serializers.CharField()
    term = serializers.IntegerField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Travel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.term = validated_data.get('term', instance.term)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

class HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    stars_number = serializers.IntegerField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.stars_number = validated_data.get('stars_number', instance.stars_number)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class KlassSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Klass.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance