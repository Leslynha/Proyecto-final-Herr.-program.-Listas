# Archivo de funciones para el algoritmo de listas
# Aquí van todas las funciones que el grupo desarrolle

def ordenar_lista(lista):
    """
    Ordena una lista de números de menor a mayor
    """
    return sorted(lista)

def buscar_elemento(lista, elemento):
    """
    Busca un elemento en la lista
    Retorna la posición si lo encuentra, -1 si no
    """
    try:
        return lista.index(elemento)
    except ValueError:
        return -1

def invertir_lista(lista):
    """
    Invierte el orden de los elementos
    """
    return lista[::-1]

def suma_lista(lista):
    """
    Calcula la suma de todos los elementos
    """
    return sum(lista)

def promedio_lista(lista):
    """
    Calcula el promedio de los elementos
    """
    if len(lista) == 0:
        return 0
    return suma_lista(lista) / len(lista)

# Agrega más funciones aquí según necesiten
