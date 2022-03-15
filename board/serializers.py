from rest_framework import serializers

from .models import Board, Category, Comment


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'created_at', 'updated_at', 'user_name', 'content', 'category_id']


class BoardPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        category = serializers.PrimaryKeyRelatedField(
            many=True, queryset=Category.objects.all()
        )
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'created_at', 'updated_at', 'user_name', 'reply', 'board_id', 'parents_id']

