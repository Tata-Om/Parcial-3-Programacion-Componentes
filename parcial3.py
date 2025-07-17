#componente 
class Product: #este producto es un componente que tendrá un nombre, una cantidad y un precio
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Producto: {self.name} | Cantidad: {self.quantity} | Precio: ${self.price:.2f}"

#componente2
class Inventory: #este inventario es un componente y tendrá la lista de productos 
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]

    def list_products(self):
        for product in self.products:
            print(product)

#componente3

