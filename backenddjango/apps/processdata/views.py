from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serizlizers import ProductSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def process_products(request):
    """list all products or save new product
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
