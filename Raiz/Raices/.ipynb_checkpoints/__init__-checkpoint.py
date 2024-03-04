from .Raices.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio

from .biseccion import biseccion, raiz_b
from .Newton import Newton, raiz_N 
from .punto_fijo import punto_fijo, raiz_fija
from .secante1 import secante1, raiz_secante1
from .secante2 import secante2, raiz_secante2

__all__ = ['es_flotante', 'intr_int', 'sigma', 'localizador', 'suma', 'derivada', 'Dominio', 'biseccion', 'raiz_b', 'Newton', 'raiz_N', 'punto_fijo', 'raiz_fija', 'secante1', 'raiz_secante1', 'secante2', 'raiz_secante2']