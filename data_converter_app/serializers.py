from rest_framework import serializers
from .models import StreamingContent

class StreamingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingContent
        fields = '__all__'