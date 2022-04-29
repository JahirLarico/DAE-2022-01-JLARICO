from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from .models import *
from tienda.carrito import Cart
# Create your views here.

def index (request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.order_by('nombre')[:6]
    context = {
        'product_list':product_list,
        'categorias':categorias
    }
    return render(request,'index.html',context)

def producto(request,producto_id):
    producto=get_object_or_404(Producto,pk=producto_id)
    categorias = Categoria.objects.order_by('nombre')[:6]
    context = {
        'producto':producto,
        'categorias':categorias
    }
    return render(request,'producto.html',context)

def categoria(request,categoria_id):
    productos = Producto.objects.filter(categoria=categoria_id).order_by('nombre')
    categorias = Categoria.objects.order_by('nombre')[:6]
    context = {
        'productos':productos,
        'categorias':categorias
    }
    return render(request,'categoria.html',context)

def carrito(request):
    return render(request,'carrito.html')

def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    return render(request,'carrito.html')


