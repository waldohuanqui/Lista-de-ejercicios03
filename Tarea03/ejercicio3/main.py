import opciones

opciones_menu = [
    {"titulo": "Dividir", "accion": opciones.opcion_dividir},
    {"titulo": "Salir", "accion": exit}
]

if __name__ == "__main__":
    while True:
        for i, opcion in enumerate(opciones_menu):
            print(f"{i + 1}. {opcion['titulo']}") # para mostrar opciones
        seleccion = int(input("Seleccione una opción: "))# ára seleccionar un opcion
        accion = opciones_menu[seleccion - 1]["accion"] #Ejecutar
        accion()