from django.urls import path
from .views import CheckListListCreateView

urlpatterns = [
    path('checklist/', CheckListListCreateView.as_view(), name='checklist-list-create'),
]
