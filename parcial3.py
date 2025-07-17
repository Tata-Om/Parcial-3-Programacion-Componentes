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
        if not self.products:
            print("No hay productos en el inventario.")
        for product in self.products:
            print(product)

#componente3 Inventory manager
 
class InventoryManager:
    def __init__(self):
        self.inventory = Inventory()

    def menu(self):
        while True:
            print("\n1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Ver inventario")
            print("4. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                name = input("Nombre del producto: ")
                quantity = int(input("Cantidad: "))
                price = float(input("Precio: "))
                product = Product(name, quantity, price)
                self.inventory.add_product(product)
                print(f"{name} agregado al inventario.")
            elif opcion == '2':
                name = input("Nombre del producto a eliminar: ")
                self.inventory.remove_product(name)
                print(f"{name} eliminado del inventario (si existía).")
            elif opcion == '3':
                print("\nInventario actual:")
                self.inventory.list_products()
            elif opcion == '4':
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida, intenta de nuevo.")
if __name__ == "__main__":
    manager = InventoryManager()
    manager.menu()

