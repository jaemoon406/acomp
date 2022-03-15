import bcrypt

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from board.serializers import BoardSerializer, BoardPostSerializer, CommentSerializer
from board.models import Board, Comment, Category


class CommentAPIView(APIView):
    def post(self, request, board_id):
        password = bcrypt.hashpw(request.data.get('password').encode('utf-8'), bcrypt.gensalt()).decode()

        new_post = {
            "user_name": request.data.get('user_name'),
            "password": password,
            "reply": request.data.get('reply'),
            "board": board_id,
            "parents": request.data.get('parents_id'),
        }
        comment = CommentSerializer(data=new_post)
        comment.is_valid(raise_exception=True)
        comment.save()

    # def get(self,request,board_id):
