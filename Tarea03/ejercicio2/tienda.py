class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, codigo, nombre, precio):
        producto = Producto(codigo, nombre, precio)
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: {producto.precio}")
        

catalogo = Catalogo()
catalogo.agregar_producto("001", "Bateria para automovil", 100.0)
catalogo.agregar_producto("002", "Aceite para motor", 50.0)
catalogo.agregar_producto("003", "Filtro de aire", 20.0)
catalogo.mostrar_productos()