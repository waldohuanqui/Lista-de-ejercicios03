def dividir(a, b):
    if b ==0:
        return "Indeterminado"
    else:
        return a/b

def opcion_dividir():
    a = float(input("Ingrese el numerador: "))
    b = float(input("Ingrese el denominador: "))
    resultado = dividir(a, b)
    print(f"El resultado de la división es: {resultado}")

