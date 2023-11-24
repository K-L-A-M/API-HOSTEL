
from django.urls import path, re_path
from .views import ManageFavoriteRoomsView, RoomListCreateView, RoomRetrieveUpdateDestroyView, ManageRoomBedsView, BedListCreateView, BedTypeListView, BedDetailView, RoomFeatureListCreateView, ManageRoomFeaturesView

urlpatterns = [
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    re_path(r'rooms/(?P<id>[0-9a-fA-F]{32,36})/$', RoomRetrieveUpdateDestroyView.as_view(), name='room-retrieve-update-destroy'),
    re_path(r'rooms/(?P<room_id>[0-9a-fA-F]{32,36})/user/(?P<id>[0-9a-fA-F]{32,36})/$', ManageFavoriteRoomsView.as_view(), name='manage-favorite-room'),
    re_path(r'rooms/(?P<room_id>[a-fA-F0-9-]+)/bed/(?P<bed_id>[a-fA-F0-9-]+)/$', ManageRoomBedsView.as_view(), name='manage-room-beds'),
    path('beds/', BedListCreateView.as_view(), name='beds-list-create'),
    path('beds/type/<bed_type>/', BedTypeListView.as_view(), name='bed-type'),
    re_path(r'beds/(?P<id>[a-fA-F0-9]{32,36})/$', BedDetailView.as_view(), name='bed-detail'),
    path('rooms/features/', RoomFeatureListCreateView.as_view(), name='room-features-list-create'),
    re_path(r'rooms/(?P<room_id>[a-fA-F0-9-]+)/feature/(?P<feature_id>[a-fA-F0-9-]+)/$', ManageRoomFeaturesView.as_view(), name='manage-room-features'),
]
