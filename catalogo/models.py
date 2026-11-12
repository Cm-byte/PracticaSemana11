"""Modelos de la app catalogo."""
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class ProductoQuerySet(models.QuerySet):
    """Consultas reutilizables del modelo Producto (lógica de negocio en el modelo)."""

    def disponibles(self):
        return self.filter(disponible=True)

    def destacados(self):
        return self.disponibles().filter(destacado=True)

    def de_categoria(self, categoria):
        return self.filter(categoria=categoria)


class Producto(models.Model):
    """Producto del catálogo FoodDelivery."""

    class Categoria(models.TextChoices):
        HAMBURGUESAS = 'Hamburguesas', 'Hamburguesas'
        PIZZAS = 'Pizzas', 'Pizzas'
        POLLO = 'Pollo', 'Pollo'
        ACOMPANAMIENTOS = 'Acompañamientos', 'Acompañamientos'
        ENSALADAS = 'Ensaladas', 'Ensaladas'
        POSTRES = 'Postres', 'Postres'
        BEBIDAS = 'Bebidas', 'Bebidas'

    nombre = models.CharField('nombre', max_length=100)
    descripcion = models.TextField('descripción', blank=True)
    categoria = models.CharField(
        'categoría', max_length=30, choices=Categoria.choices, default=Categoria.HAMBURGUESAS
    )
    precio = models.DecimalField(
        'precio (S/)', max_digits=8, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
    )
    imagen_url = models.URLField('URL de la imagen', blank=True)
    disponible = models.BooleanField('disponible', default=True)
    destacado = models.BooleanField('destacado', default=False)
    fecha_creacion = models.DateTimeField('fecha de creación', auto_now_add=True)

    objects = ProductoQuerySet.as_manager()

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['categoria', 'nombre']

    def __str__(self):
        return f'{self.nombre.title()} - S/ {self.precio}'