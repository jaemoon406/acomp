from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/user', include('user.urls')),
    path('api/board', include('board.urls'))
]

