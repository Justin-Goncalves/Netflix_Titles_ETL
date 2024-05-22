from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
import pandas

# Create your views here.
@api_view(['GET', 'POST'])
def StreamingContent_details(request):
    if request.method == "GET":
        streamingcontents = StreamingContent.objects.all()
        serializer = StreamingContentSerializer(streamingcontents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if request.FILES:
            data_df = pandas.read_csv(request.FILES['data'])
            data_list = data_df.to_dict(orient="records")
            serializer = StreamingContentSerializer(data={'data': data_list}, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response('Successfully Uploaded')
        else:
            return Response('No file uploaded.', status=status.HTTP_400_BAD_REQUEST)