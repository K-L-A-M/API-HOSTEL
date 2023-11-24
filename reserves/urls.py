from django.urls import path, re_path
from .views import ReservationListCreateView, ReservationDetailView

urlpatterns = [
    path('reservations/', ReservationListCreateView.as_view(), name='reservation-list-create'),
    re_path(r'^reservations/(?P<pk>[a-f0-9]+)/$', ReservationDetailView.as_view(), name='reservation-detail'),
]
