#componente 
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Producto: {self.name} | Cantidad: {self.quantity} | Precio: ${self.price:.2f}"




