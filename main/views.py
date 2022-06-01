from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


from .models import Product
from .serializers import ProductSerializer

class ProductAPIView(APIView):

    def get(self, request):
        search = request.query_params.get('search')
        if search:
            products = Product.objects.filter(Q(title__icontains=search) | Q(price__icontains=search), is_published=True)
        else:
            products = Product.objects.filter(is_published=True).order_by('title')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RetrieveProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer


class DestroyProductView(generics.DestroyAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer


class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer


class CreateProductView(generics.CreateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
