import uuid
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from users.serializers import UserSerializer
from .models import Room, RoomFeature
from .serializers import RoomFeatureSerializer, RoomSerializer
from users.permissions import IsAnyUserPermission, IsManagerOrAdministratorPermission, IsOwnerOrEmployeeOrManagerOrAdministratorPermission, IsEmployeeOrManagerOrAdministratorPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Bed
from .serializers import BedSerializer


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAnyUserPermission]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsManagerOrAdministratorPermission()]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RoomRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAnyUserPermission]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsManagerOrAdministratorPermission()]
        return super().get_permissions()

    def get_object(self):
        room_id = self.kwargs.get("id")

        if room_id is None:
            raise Http404("Room not found")

        try:
            room_id = uuid.UUID(room_id.replace("-", ""))
        except ValueError:
            raise Http404("Invalid room ID")

        return get_object_or_404(Room, id=room_id)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManageFavoriteRoomsView(APIView):
    permission_classes = [IsOwnerOrEmployeeOrManagerOrAdministratorPermission]
    lookup_field_user = 'id'
    lookup_field_room = 'id'

    def convert_hex_to_uuid(self, value):
        return uuid.UUID(value)

    def post(self, request, id, room_id):
        user = request.user

        if str(self.convert_hex_to_uuid(id)) != str(user.id):
            return Response({'error': 'Invalid user ID'}, status=status.HTTP_403_FORBIDDEN)

        room = get_object_or_404(Room, **{self.lookup_field_room: self.convert_hex_to_uuid(room_id)})

        if room in user.favorite_rooms.all():
            return Response({'error': 'Room already in favorites'}, status=status.HTTP_400_BAD_REQUEST)

        user.favorite_rooms.add(room)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id, room_id):
        user = request.user

        if str(self.convert_hex_to_uuid(id)) != str(user.id):
            return Response({'error': 'Invalid user ID'}, status=status.HTTP_403_FORBIDDEN)

        room = user.favorite_rooms.filter(id=self.convert_hex_to_uuid(room_id)).first()

        if room is None:
            return Response({'error': 'Room not in favorites'}, status=status.HTTP_400_BAD_REQUEST)

        user.favorite_rooms.remove(room)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BedListCreateView(generics.ListCreateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsManagerOrAdministratorPermission()]
        elif self.request.method == 'GET':
            return [IsAnyUserPermission()]
        return super().get_permissions()


class ManageRoomBedsView(APIView):
    permission_classes = [IsManagerOrAdministratorPermission]
    lookup_field_room = 'id'
    lookup_field_bed = 'id'

    def convert_hex_to_uuid(self, value):
        return uuid.UUID(value)

    def post(self, request, room_id, bed_id):
        room = get_object_or_404(Room, **{self.lookup_field_room: self.convert_hex_to_uuid(room_id)})
        bed = get_object_or_404(Bed, **{self.lookup_field_bed: self.convert_hex_to_uuid(bed_id)})

        if bed in room.beds.all():
            return Response({'error': 'Bed already in the room'}, status=status.HTTP_400_BAD_REQUEST)

        room.beds.add(bed)
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, room_id, bed_id):
        room = get_object_or_404(Room, **{self.lookup_field_room: self.convert_hex_to_uuid(room_id)})
        bed = room.beds.filter(**{self.lookup_field_bed: self.convert_hex_to_uuid(bed_id)}).first()

        if bed is None:
            return Response({'error': 'Bed not in the room'}, status=status.HTTP_400_BAD_REQUEST)

        room.beds.remove(bed)
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BedTypeListView(generics.ListAPIView):
    serializer_class = BedSerializer
    permission_classes = [IsAnyUserPermission]

    def get_queryset(self):
        bed_type = self.kwargs.get('bed_type')
        return Bed.objects.filter(bed_type=bed_type)


class BedDetailView(generics.RetrieveAPIView):
    serializer_class = BedSerializer
    permission_classes = [IsAuthenticated, IsEmployeeOrManagerOrAdministratorPermission]
    lookup_field = 'id'

    def get_object(self):
        bed_id = self.kwargs.get(self.lookup_field)
        try:
            bed_id = uuid.UUID(bed_id)
        except ValueError:
            raise Http404("Invalid bed ID")

        return get_object_or_404(Bed, id=bed_id)


class RoomFeatureListCreateView(generics.ListCreateAPIView):
    queryset = RoomFeature.objects.all()
    serializer_class = RoomFeatureSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsManagerOrAdministratorPermission()]
        elif self.request.method == 'GET':
            return [IsAnyUserPermission()]
        return super().get_permissions()


class ManageRoomFeaturesView(APIView):
    permission_classes = [IsManagerOrAdministratorPermission]
    lookup_field_room = 'id'
    lookup_field_feature = 'id'

    def convert_hex_to_uuid(self, value):
        return uuid.UUID(value)

    def post(self, request, room_id, feature_id):
        room = get_object_or_404(Room, **{self.lookup_field_room: self.convert_hex_to_uuid(room_id)})
        feature = get_object_or_404(RoomFeature, **{self.lookup_field_feature: self.convert_hex_to_uuid(feature_id)})

        if feature in room.features.all():
            return Response({'error': 'Feature already in the room'}, status=status.HTTP_400_BAD_REQUEST)

        room.features.add(feature)
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, room_id, feature_id):
        room = get_object_or_404(Room, **{self.lookup_field_room: self.convert_hex_to_uuid(room_id)})
        feature = room.features.filter(**{self.lookup_field_feature: self.convert_hex_to_uuid(feature_id)}).first()

        if feature is None:
            return Response({'error': 'Feature not in the room'}, status=status.HTTP_400_BAD_REQUEST)

        room.features.remove(feature)
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)
