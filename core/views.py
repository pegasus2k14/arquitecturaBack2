from rest_framework import generics
from .serializers import ProductosSerializer
from .models import Productos
from rest_framework.permissions import AllowAny

class ProductosList(generics.ListAPIView):
    #select * from productos
    queryset = Productos.objects.all()
    serializer_class=ProductosSerializer
    #Para q todos tengan permisos de acceder a los endpoints sin token
    #permission_classes =(AllowAny,)
