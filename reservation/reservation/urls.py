from django.contrib import admin
from django.urls import path
from reservation.reservation_app.views import AddRoomView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/new/', AddRoomView.as_view(), name="add-room"),
]
