from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from product.models import Category,Product
from .serializers import CategorySerializer,ProductSerializer
from django.contrib.auth.decorators import login_required

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@api_view(['GET'])
@login_required
def get_products(request):
    products=Product.objects.all()
    print(products)
    serialize=ProductSerializer(products,many=True)
    print(serialize.data)
    return Response(serialize.data)




