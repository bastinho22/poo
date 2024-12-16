from rest_framework import viewsets
from inventario.models import Producto
from inventario.api.serializer import ProductoSerializer
from rest_framework.permissions import IsAuthenticated


class productoviewset(viewsets.ModelViewSet):
    permission_classes =[IsAuthenticated]
    queryset =Producto.objects.all()
    serializer_class=ProductoSerializer
    