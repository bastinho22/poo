from rest_framework import viewsets
from inventario.models import Producto

from inventario.api.serializer import ProductoSerializer

class productoviewset(viewsets.ModelViewSet):
    queryset =Producto.objects.all()
    serializer_class=ProductoSerializer