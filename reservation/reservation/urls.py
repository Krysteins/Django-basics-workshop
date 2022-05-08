from django.contrib import admin
from django.urls import path
from reservation_app.views import AddRoomView, RoomListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/new/', AddRoomView.as_view(), name="add-room"),
    path('', RoomListView.as_view(), name="room-list"),
]
