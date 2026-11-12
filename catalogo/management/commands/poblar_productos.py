from decimal import Decimal

from django.core.management.base import BaseCommand

from catalogo.models import Producto

UNSPLASH = 'https://images.unsplash.com/photo-{}?w=600'

PRODUCTOS = [
    {
        'nombre': 'hamburguesa clásica',
        'descripcion': 'Carne de res a la parrilla, queso cheddar, lechuga, tomate y salsa de la casa.',
        'categoria': Producto.Categoria.HAMBURGUESAS,
        'precio': Decimal('18.90'),
        'imagen_url': UNSPLASH.format('1568901346375-23c9450c58cd'),
        'destacado': True,
    },
    {
        'nombre': 'hamburguesa royal',
        'descripcion': 'Doble carne, huevo frito, plátano frito, queso y papas al hilo.',
        'categoria': Producto.Categoria.HAMBURGUESAS,
        'precio': Decimal('24.50'),
        'imagen_url': UNSPLASH.format('1550547660-d9450f859349'),
    },
    {
        'nombre': 'pizza americana familiar',
        'descripcion': 'Masa artesanal, salsa de tomate, mozzarella y jamón. 8 tajadas.',
        'categoria': Producto.Categoria.PIZZAS,
        'precio': Decimal('39.90'),
        'imagen_url': UNSPLASH.format('1513104890138-7c749659a591'),
        'destacado': True,
    },
    {
        'nombre': 'pollo broaster 1/4',
        'descripcion': 'Cuarto de pollo crocante con papas fritas, ensalada y cremas.',
        'categoria': Producto.Categoria.POLLO,
        'precio': Decimal('16.00'),
        'imagen_url': UNSPLASH.format('1626082927389-6cd097cdc6ec'),
        'destacado': True,
    },
    {
        'nombre': 'salchipapa especial',
        'descripcion': 'Papas fritas con hot dog, chorizo, huevo y cremas al gusto.',
        'categoria': Producto.Categoria.ACOMPANAMIENTOS,
        'precio': Decimal('14.50'),
        'imagen_url': UNSPLASH.format('1573080496219-bb080dd4f877'),
    },
    {
        'nombre': 'ensalada césar',
        'descripcion': 'Lechuga romana, pollo a la plancha, crutones, parmesano y aderezo césar.',
        'categoria': Producto.Categoria.ENSALADAS,
        'precio': Decimal('19.90'),
        'imagen_url': UNSPLASH.format('1512621776951-a57141f2eefd'),
    },
    {
        'nombre': 'copa de helado',
        'descripcion': 'Tres bolas de helado artesanal con fudge y galleta.',
        'categoria': Producto.Categoria.POSTRES,
        'precio': Decimal('9.90'),
        'imagen_url': UNSPLASH.format('1563805042-7684c019e1cb'),
        'disponible': False,  # agotado
    },
    {
        'nombre': 'limonada frozen',
        'descripcion': 'Limonada frapeada de 500 ml, con hierbabuena.',
        'categoria': Producto.Categoria.BEBIDAS,
        'precio': Decimal('7.50'),
        'imagen_url': UNSPLASH.format('1622483767028-3f66f32aef97'),
    },
]


class Command(BaseCommand):
    help = 'Carga productos de ejemplo en el catálogo FoodDelivery'

    def handle(self, *args, **options):
        creados = 0
        for datos in PRODUCTOS:
            datos = {'disponible': True, 'destacado': False, **datos}
            _, creado = Producto.objects.update_or_create(
                nombre=datos.pop('nombre'), defaults=datos
            )
            creados += creado

        total = Producto.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'[OK] {creados} producto(s) creado(s). Total en la base de datos: {total}'
        ))