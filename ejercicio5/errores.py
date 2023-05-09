import os

try:
    import producto
except ImportError:
    print("No se pudo importar el módulo producto")

else:
    print("Módulo producto importado exitosmente")
    print("Directorio de trabajo:", os.getcwd())

    p = producto.p

    print(p)

finally:
    print("Proceso terminado")