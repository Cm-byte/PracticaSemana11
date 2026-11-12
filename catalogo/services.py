"""Capa de servicios del catálogo FoodDelivery.

Las vistas llaman a estas funciones; aquí se usa el ORM de Django
(los filtros reutilizables están en ProductoQuerySet, en models.py).
"""
from django.db.models import Min

from .models import Producto


def obtener_productos(categoria=None):
    """Productos disponibles; si se indica categoría, solo los de esa categoría."""
    productos = Producto.objects.disponibles()
    if categoria:
        productos = productos.de_categoria(categoria)
    return productos


def obtener_destacados(limite=3):
    """Productos disponibles marcados como destacados (para la portada)."""
    return Producto.objects.destacados()[:limite]


def obtener_producto(pk):
    """Un producto disponible por su ID, o None si no existe."""
    return Producto.objects.disponibles().filter(pk=pk).first()


def obtener_categorias():
    """Lista ordenada de categorías que tienen productos disponibles."""
    return list(
        Producto.objects.disponibles()
        .order_by('categoria')
        .values_list('categoria', flat=True)
        .distinct()
    )


def resumen_catalogo():
    """Datos generales para la portada."""
    disponibles = Producto.objects.disponibles()
    return {
        'total_productos': disponibles.count(),
        'total_categorias': len(obtener_categorias()),
        'precio_minimo': disponibles.aggregate(minimo=Min('precio'))['minimo'] or 0,
    }