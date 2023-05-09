class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        pais, lote, año = self.codigo.split('-')
        return f"Producto: {self.nombre}\nCódigo: {self.codigo}\nPaís de origen: {pais}\nNúmero de lote: {lote}\nAño: {año}"


nombre = input("Ingrese el nombre del producto: ")
codigo = input("Ingrese el código del producto en formato 'PAIS-LOTE-AÑO': ")

p = Producto(nombre, codigo)
