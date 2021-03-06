from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

#############################################################################
#----------------------------Function Based View----------------------------#

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     """
#     List of all snippets, or create a new snippet. 
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         group_serializer = SnippetSerializer(snippets, many=True)
#         # return(JsonResponse(group_serializer.data, safe=False))
#         return(Response(group_serializer.data))

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             # return(JsonResponse(serializer.data, status=201))
#             return(Response(serializer.data, status=status.HTTP_201_CREATED))
#         # return(JsonResponse(serializer.errors, status=400))
#         return(Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST))


# # @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     """
#     Fetch Snippet, Update Snippet, Delete Snippet
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         # return(HttpResponse(status=404))
#         return(Response(status=status.HTTP_404_NOT_FOUND))

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         # return(JsonResponse(serializer.data))
#         return(Response(serializer.data))

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             # return(JsonResponse(serializer.data, status=200))
#             return(Response(serializer.data, status=status.HTTP_200_OK))
#         else:
#             # return(JsonResponse(serializer.errors, status=400))
#             return(Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST))

#     elif request.method == 'DELETE':
#         snippet.Delete()
#         # return(HttpResponse(status=204))
#         return(Response(status=status.HTTP_204_NO_CONTENT))


#############################################################################
#----------------------------------APIVIEW----------------------------------#
# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return(Response(serializer.data))
    
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return(Response(serializer.data, status=status.HTTP_201_CREATED))
#         else:
#             return(Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST))


# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return(Snippet.objects.get(pk=pk))
#         except Snippet.DoesNotExist:
#             return(Http404)

#     def get(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return(Response(serializer.data))
    
#     def put(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return(Response(serializer.data, status=status.HTTP_200_OK))
#         else:
#             return(Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST))
    
#     def delete(self, pk):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return(Response(status=status.HTTP_204_NO_CONTENT))


#############################################################################
#-----------------------Using Mixins & GenericAPIView-----------------------#
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     """
#      List all snippets, or create a new snippet.
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return(self.list(request, *args, **kwargs))

#     def post(self, request, *args, **kwargs):
#         return(self.create(request, *args, **kwargs))

# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return(self.retrieve(request, *args, **kwargs))

#     def put(self, request, *args, **kwargs):
#         return(self.update(request, *args, **kwargs))

#     def delete(self, request, *args, **kwargs):
#         return(self.destroy(request, *args, **kwargs))


#############################################################################
#----------------------Using generic class-based views----------------------#
class SnippetList(generics.ListCreateAPIView):
    """
     List all snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
