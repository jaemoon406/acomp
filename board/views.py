import bcrypt

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BoardSerializer
from .models import Board


class BoardListAPIView(APIView):
    def get(self, request, category_id):
        OFFSET = int(request.GET.get('OFFSET', 0))
        LIMIT = int(request.GET.get('LIMIT', 5))

        board = Board.objects.filter(category_id=category_id)
        serializer = BoardSerializer(board, many=True)

        return Response(serializer.data[OFFSET: OFFSET + LIMIT], status=status.HTTP_200_OK)


class BoardDetailAPIView(APIView):
    def get(self, request, board_id):
        board = Board.objects.get(id=board_id)
        serializer = BoardSerializer(board)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,category_id):

        new_post = {
            'user_name': request.data.get('user_name'),
            'password': request.data.get('user_name'),
            'content': request.data.get('content'),
            'category_id': category_id
        }
        board = BoardSerializer(new_post)

        '''
        is_valid 사용하는법 알고 수정
        '''
        board.is_valid(user_name=request.data.get('user_name'))
        board.save()
