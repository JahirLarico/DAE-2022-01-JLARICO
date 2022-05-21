from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Producto
from .serializers import ProductoSerializer
# Create your views here.
class IndexView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)