from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CheckList
from .serializers import CheckListSerializer
from users.permissions import IsEmployeeOrManagerOrAdministratorPermission


class CheckListListCreateView(generics.ListCreateAPIView):
    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsEmployeeOrManagerOrAdministratorPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
