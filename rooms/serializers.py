from rest_framework import serializers
from .models import BedType, Room, RoomFeature, Bed
from promotions.serializers import PromotionSerializer
from babel.numbers import format_currency


class RoomFeatureSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)

    class Meta:
        model = RoomFeature
        fields = ['id', 'name']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class BedSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    bed_type = serializers.ChoiceField(choices=BedType.choices, default=BedType.SINGLE)

    class Meta:
        model = Bed
        fields = ['id', 'bed_type', 'quantity']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class RoomSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    promotions = PromotionSerializer(many=True, read_only=True)
    beds = BedSerializer(many=True, read_only=True)
    features = RoomFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'floor', 'room_number', 'capacity', 'is_occupied', 'price_per_night', 'promotions', 'beds', 'features']
        extra_kwargs = {
            'id': {'read_only': True},
            'promotions': {'read_only': True},
            'beds': {'read_only': True},
            'features': {'read_only': True},
        }

    def get_formatted_price_per_night(self, obj):
        return format_currency(obj.price_per_night, 'BRL', locale='pt_BR')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        formatted_price = self.get_formatted_price_per_night(instance)
        representation['price_per_night'] = formatted_price

        return representation
