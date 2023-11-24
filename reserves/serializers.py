from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    user = serializers.UUIDField(source='user_id', format='hex')
    room = serializers.UUIDField(source='room_id', format='hex')

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'room', 'check_in_date', 'check_out_date', 'is_paid', 'transaction']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user_id.hex
        return representation

    def to_internal_value(self, data):
        user_uuid = data.get('user')
        if isinstance(user_uuid, str):
            data['user'] = user_uuid

        return super().to_internal_value(data)
