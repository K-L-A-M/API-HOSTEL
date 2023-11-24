from rest_framework import serializers

from users.models import User
from .models import Transaction
import pytz


class TransactionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    user_name = serializers.CharField(read_only=True, source='user.username')
    user_cpf = serializers.CharField(read_only=True, source='user.cpf')

    class Meta:
        model = Transaction
        fields = [
            'id',
            'user',
            'user_name',
            'user_cpf',
            'method',
            'timestamp',
            'amount_paid',
            'discount_percentage',
            'discount_amount',
        ]
        read_only_fields = ['id', 'timestamp', 'user_name', 'user_cpf',]
        extra_kwargs = {
            "discount_percentage": {"required": False},
            "discount_amount": {"required": False}
        }

    def get_user(self, obj):
        if obj.user:
            return obj.user.id
        return None

    def get_timestamp(self, obj):
        if isinstance(obj, Transaction):
            timestamp = obj.timestamp
            if timestamp:
                tz = pytz.timezone('America/Sao_Paulo')
                timestamp = timestamp.astimezone(tz)
                return timestamp.strftime('%d-%m-%YT%H:%M:%S.%fZ')
        return None

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        user = User.objects.get(id=user_id)

        transaction = Transaction.objects.create(
            user=user,
            user_name=user.name,
            user_cpf=user.cpf,
            method=validated_data['method'],
            timestamp=validated_data.get('timestamp'),
            amount_paid=validated_data.get('amount_paid', 0),
            discount_percentage=validated_data.get('discount_percentage', 0),
            discount_amount=validated_data.get('discount_amount', 0)
        )

        return transaction
