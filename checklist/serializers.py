from rest_framework import serializers
from .models import CheckList


class CheckListSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    user = serializers.UUIDField(format='hex')
    room = serializers.UUIDField(format='hex')
    check_in_date = serializers.DateField(required=False)
    check_out_date = serializers.DateField(required=False)

    class Meta:
        model = CheckList
        fields = [
            'id',
            'user',
            'room',
            'check_in_date',
            'check_out_date',

        ]
        read_only_fields = ['id']
