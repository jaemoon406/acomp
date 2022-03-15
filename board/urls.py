from django.urls import path
from board.views.board_views import *
from board.views.comment_views import *
from board.views.search_views import *

urlpatterns = [
    path('detail/<int:board_id>', BoardDetailAPIView.as_view()),
    path('<int:category_id>/boardlist', BoardListAPIView.as_view()),
    path('boardpost', BoardPostAPIView.as_view()),
]