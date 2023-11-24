from django.urls import path, re_path
from .views import ManageRoomPromotionsView, PromotionListCreateView, PromotionRetrieveUpdateDestroyView

urlpatterns = [
    path('promotions/', PromotionListCreateView.as_view(), name='promotion-list-create'),
    re_path(r'^promotions/(?P<pk>[a-f\d]{32})/$', PromotionRetrieveUpdateDestroyView.as_view(), name='promotion-retrieve-update-destroy'),
    re_path(r'^promotions/(?P<promotion_id>[a-f0-9-]+)/rooms/(?P<room_id>[a-f0-9-]+)/$', ManageRoomPromotionsView.as_view(), name='manage-room-promotions'),
]
