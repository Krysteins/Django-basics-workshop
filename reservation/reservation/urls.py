from django.contrib import admin
from django.urls import path
from reservation_app.views import AddRoomView, RoomListView, DeleteRoomView, ModifyRoomView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/new/', AddRoomView.as_view(), name="add-room"),
    path('', RoomListView.as_view(), name="room-list"),
    path('room/delete/<int:room_id>/', DeleteRoomView.as_view(), name="delete-room"),
    path('room/modify/<int:room_id>/', ModifyRoomView.as_view(), name="modify-room"),
]
