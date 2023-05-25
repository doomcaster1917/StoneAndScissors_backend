from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("websocket.urls")),
    path('api/', include('authentication.urls', namespace='authentication')),
]