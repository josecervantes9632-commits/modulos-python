class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        return self.precio * self.cantidad

    def resumen(self):
        return (f"{self.nombre}: {self.cantidad} piezas a ${self.precio:.2f} "
                f"= ${self.valor_total():.2f} en inventario")
