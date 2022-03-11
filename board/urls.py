from django.urls import include, path
from board.views import *

urlpatterns = [
    path('/detail/<int:board_id>', BoardDetailAPIView.as_view()),
    path('/<int:category_id>/boardlist', BoardListAPIView.as_view())
]