import bcrypt

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from board.serializers import BoardSerializer, BoardPostSerializer
from board.models import Board


class BoardListAPIView(APIView):
    def get(self, request, category_id):
        """
        게시물 전체를 보여주는 리스트 API
        한 페이지당 5개의 게시물을 보여준다.
        """
        OFFSET = int(request.GET.get('OFFSET', 0))
        LIMIT = int(request.GET.get('LIMIT', 5))

        board = Board.objects.filter(category_id=category_id)
        serializer = BoardSerializer(board, many=True)

        return Response(serializer.data[OFFSET: OFFSET + LIMIT], status=status.HTTP_200_OK)


class BoardDetailAPIView(APIView):
    def get(self, request, board_id):
        """
        선택한 게시물을 보여주는 API
        """
        board = Board.objects.get(id=board_id)
        serializer = BoardSerializer(board)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, board_id):
        board = Board.objects.get(id=board_id)

        if bcrypt.checkpw(request.data.get('password').encode('utf-8'),
                          board.password.encode('utf-8')):
            serializer = BoardSerializer(board, data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response('asdfasdf', status=status.HTTP_400_BAD_REQUEST)
        return Response('123123123', status=status.HTTP_401_UNAUTHORIZED)


class BoardPostAPIView(APIView):
    def post(self, request):
        """
        게시물 작성 API
        계정 설정을 따로 하지 않아
        user_name과 password를 요청에 받는다.
        """

        password = bcrypt.hashpw(request.data.get('password').encode('utf-8'), bcrypt.gensalt()).decode()
        new_post = {
            'user_name': request.data.get('user_name'),
            'content': request.data.get('content'),
            'category': request.data.get('category_id'),
            'password': password,
        }
        board = BoardPostSerializer(data=new_post)
        board.is_valid(raise_exception=True)
        board.save()

        return Response('success', status=status.HTTP_201_CREATED)

