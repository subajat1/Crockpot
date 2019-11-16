from django.utils.text import slugify

from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models

class UploadStoresView(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request, filename, format=None):
        chunked = ''
        for chunk in request.FILES['file'].chunks():
            chunked += chunk.decode("utf-8") 

        data = chunked.split('\n')
        data = data[1:len(data)-1]
        for d in data:
            rows = d.split(',')
            store = models.Store(
                name=rows[0],
                slug=slugify(rows[0]),
                icon=rows[1],
                media=rows[2],
            )
            store.save()
        return Response(status=204)
    
class UploadCategoriesView(APIView):
    parser_classes = (MultiPartParser,)
    
    def put(self, request, filename, format=None):
        chunked = ''
        for chunk in request.FILES['file'].chunks():
            chunked += chunk.decode("utf-8") 

        data = chunked.split('\n')
        data = data[1:len(data)-1]
        for d in data:
            rows = d.split(',')
            category = models.Category(
                name=rows[0],
                slug=slugify(rows[0]),
                icon=rows[1],
                media=rows[2],
            )
            category.save()
        return Response(status=204)