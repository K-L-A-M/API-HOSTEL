from rest_framework import generics
from users.permissions import IsEmployeeOrManagerOrAdministratorPermission, IsOwnerOrEmployeeOrManagerOrAdministratorPermission
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Transaction


class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsOwnerOrEmployeeOrManagerOrAdministratorPermission()]
        elif self.request.method == 'GET':
            return [IsAuthenticated(), IsEmployeeOrManagerOrAdministratorPermission()]
        return super().get_permissions()

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
