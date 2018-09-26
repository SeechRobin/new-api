from rest_framework import serializers
from .models import News, Comments

class NewslistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = News
        fields = ('id', 'title','body','blurb', 'image_url','author', 'published_date', 'date_modified', 'comments')
        read_only_fields = ('published_date', 'date_modified')


class CommentsSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Comments
        fields = ('id', 'body', 'created_by')
