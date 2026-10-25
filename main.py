# Importo la clase Producto que está en otro archivo (el módulo modelos.py)
from modelos import Producto

# Creo objetos con datos de prueba
teclado = Producto("Teclado", 450.0, 10)
mouse = Producto("Mouse", 199.5, 25)

# Muestro en consola el resultado del método de la clase
print(teclado.resumen())
print(mouse.resumen())
