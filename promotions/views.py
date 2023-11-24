import uuid
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rooms.models import Room
from rooms.serializers import RoomSerializer
from users.permissions import IsAnyUserPermission, IsManagerOrAdministratorPermission
from .models import Promotion
from .serializers import PromotionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PromotionListCreateView(generics.ListCreateAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsManagerOrAdministratorPermission()]
        elif self.request.method == 'GET':
            return [IsAnyUserPermission()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save()


class PromotionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [IsManagerOrAdministratorPermission]

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        Promotion.objects.filter(end_date__lt=timezone.now()).delete()
        return response


class ManageRoomPromotionsView(APIView):
    permission_classes = [IsManagerOrAdministratorPermission]
    lookup_field_room = 'id'
    lookup_field_promotion = 'id'

    def convert_hex_to_uuid(self, value):
        return uuid.UUID(value)

    def post(self, request, room_id, promotion_id):
        room = get_object_or_404(Room, **{self.lookup_field_room: self.convert_hex_to_uuid(room_id)})
        promotion = get_object_or_404(Promotion, **{self.lookup_field_promotion: self.convert_hex_to_uuid(promotion_id)})

        if promotion in room.promotions.all():
            return Response({'error': 'Promotion already in the room'}, status=status.HTTP_400_BAD_REQUEST)

        room.promotions.add(promotion)
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, room_id, promotion_id):
        room = get_object_or_404(Room, **{self.lookup_field_room: self.convert_hex_to_uuid(room_id)})
        promotion = room.promotions.filter(**{self.lookup_field_promotion: self.convert_hex_to_uuid(promotion_id)}).first()

        if promotion is None:
            return Response({'error': 'Promotion not in the room'}, status=status.HTTP_400_BAD_REQUEST)

        room.promotions.remove(promotion)
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)
