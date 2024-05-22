from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
import pandas

# Create your views here.
@api_view(['GET', 'POST'])
def streamingcontent_details(request):
    if request.method == "GET":
        streamingcontents = StreamingContent.objects.all()
        serializer = StreamingContentSerializer(streamingcontents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if request.FILES:
            data_df = pandas.read_csv(request.FILES['netflix_data'])
            data_df['cast'] = data_df['cast'].apply(convert_to_list)
            data_df['listed_in'] = data_df['listed_in'].apply(convert_to_list)
            replaceNAN(data_df, 'director')
            replaceNAN(data_df, 'country')
            data_list = data_df.to_dict(orient='records')
            serializer = StreamingContentSerializer(data=data_list, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response('Successfully Uploaded')
        else:
            return Response('No file uploaded.', status=status.HTTP_400_BAD_REQUEST)
        
def convert_to_list(value):
    if pandas.isnull(value): 
        return []
    return value.split(',')

def replaceNAN(fileName, key):
    fileName[key] = fileName[key].replace("nan", pandas.NA).fillna('')