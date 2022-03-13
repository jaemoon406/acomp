from rest_framework import serializers

from .models import Board, Category


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
