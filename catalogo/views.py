from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from . import services


# ---------- FBV: vista basada en función ----------
def home(request):
    """Portada: muestra un resumen y los productos destacados."""
    contexto = {
        'titulo': 'Inicio',
        'destacados': services.obtener_destacados(),
        'resumen': services.resumen_catalogo(),
    }
    return render(request, 'catalogo/home.html', contexto)


# ---------- CBV: vista basada en clase ----------
class CatalogoListView(ListView):
    """Catálogo completo, con filtro opcional por categoría (?categoria=Pizzas)."""

    template_name = 'catalogo/catalogo.html'
    context_object_name = 'productos'   # en la plantilla: {% for p in productos %}

    def get_queryset(self):
        categoria = self.request.GET.get('categoria')
        return services.obtener_productos(categoria)

    def get_context_data(self, **kwargs):
        """Agrega datos extra al contexto, además de la lista de productos."""
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = 'Catálogo'
        contexto['categorias'] = services.obtener_categorias()
        contexto['categoria_actual'] = self.request.GET.get('categoria', '')
        return contexto


# ---------- FBV: detalle de un producto ----------
def detalle(request, pk):
    """Detalle de un producto; responde 404 si no existe o no está disponible."""
    producto = services.obtener_producto(pk)
    if producto is None:
        raise Http404('Producto no encontrado')
    return render(request, 'catalogo/detalle.html', {
        'titulo': producto.nombre,
        'producto': producto,
    })