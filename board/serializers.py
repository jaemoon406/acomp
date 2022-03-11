from rest_framework import serializers

from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'created_at', 'updated_at', 'user_name', 'content', 'category_id']



