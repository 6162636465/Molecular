import numpy as np
import networkx as nx
import graphviz
import matplotlib.pyplot as plt
from pyrsistent import v
import treelib
from pyparsing import with_attribute
from treelib import Node, Tree
import sys
from collections import OrderedDict
sys.setrecursionlimit(500000)
h = graphviz.Digraph('H', filename='hello.gv')
G = nx.DiGraph()
def swap_(cadena1, cadena2):
    temp = cadena1
    cadena1 = cadena2
    cadena2 = temp
    return cadena1, cadena2


def convert(lista):
    return tuple(i for i in lista)

def recorrer_matrix(matrix, x, y):
    if x == 0 and y != 0:
        G.add_edge((x, y), (x, y - 1), weight=-1)
        recorrer_matrix(matrix, x, y - 1)
    if y == 0 and x != 0:
        G.add_edge((x, y), (x - 1, y), weight=-1)
        recorrer_matrix(matrix, x - 1, y)
    if x == 0 and y == 0 or (x - 1 < 0 or y - 1 < 0):
        return 0

    cell_value = matrix[x - 1][y - 1]
    if hasattr(cell_value, '__len__'):  # Verificar si es iterable
        tam = len(cell_value)
        for i in range(1, tam):
            recorrer_matrix(matrix, cell_value[i][0], cell_value[i][1])
            G.add_edge((x, y), convert(cell_value[i]), weight=1)
    else:
        tam = 0  # No iterable, no hay elementos que recorrer
    return tam

def maximo(matriz, i, j, cadena1, cadena2):
    lista_valores = []
    lista_temp = []
    lista_temp2 = []
    lista_temp3 = []
    temp = 0

    if i == 0:
        lista_temp.append(i)
        lista_temp.append(j - 1)
        lista_valores.append(lista_temp)
        return matriz[i][j - 1], lista_valores

    elif j == 0:
        lista_temp2.append(i - 1)
        lista_temp2.append(j)
        lista_valores.append(lista_temp2)
        return matriz[i - 1][j], lista_valores

    if cadena1[j] == cadena2[i]:
        temp = 1
    else:
        temp = -1
    a = matriz[i - 1][j - 1] + (1 * temp)
    b = matriz[i][j - 1] - 2
    c = matriz[i - 1][j] - 2
    numeros = [a, b, c]

    if a == c == b and a == max(numeros):
        lista_temp.append(i - 1)
        lista_temp.append(j - 1)
        lista_valores.append(lista_temp)
        lista_temp2.append(i)
        lista_temp2.append(j - 1)
        lista_valores.append(lista_temp2)
        lista_temp3.append(i - 1)
        lista_temp3.append(j)
        lista_valores.append(lista_temp3)

    elif a == b and a == max(numeros):
        lista_temp.append(i - 1)
        lista_temp.append(j - 1)
        lista_valores.append(lista_temp)
        lista_temp2.append(i)
        lista_temp2.append(j - 1)
        lista_valores.append(lista_temp2)

    elif a == c and a == max(numeros):
        lista_temp.append(i - 1)
        lista_temp.append(j - 1)
        lista_valores.append(lista_temp)
        lista_temp3.append(i - 1)
        lista_temp3.append(j)
        lista_valores.append(lista_temp3)

    elif b == c and b == max(numeros):
        lista_temp2.append(i)
        lista_temp2.append(j - 1)
        lista_valores.append(lista_temp2)
        lista_temp3.append(i - 1)
        lista_temp3.append(j)
        lista_valores.append(lista_temp3)

    elif a == max(numeros):
        lista_temp.append(i - 1)
        lista_temp.append(j - 1)
        lista_valores.append(lista_temp)

    elif b == max(numeros):
        lista_temp.append(i)
        lista_temp.append(j - 1)
        lista_valores.append(lista_temp)

    elif c == max(numeros):
        lista_temp2.append(i - 1)
        lista_temp2.append(j)
        lista_valores.append(lista_temp2)
    return max(numeros), lista_valores

def alineamientosfun(lista_cam, lista2, cadena2, cadena1):
    cadena_temp = cadena1[1:]
    lista_temp = ''
    temp_indice = len(cadena_temp) - 1
    for i in range(0, len(lista_cam)):
        for j in range(0, len(lista_cam[0]) - 1):
            if lista_cam[i][j] == lista_cam[i][j + 1] + 1 or lista_cam[i][j] == lista_cam[i][j + 1] - 1:
                lista_temp += cadena_temp[temp_indice]
                temp_indice -= 1

            else:
                lista_temp += '-'
        lista2.append(lista_temp[::-1])
        temp_indice = len(cadena_temp) - 1
        lista_temp = ''
    return lista2

def bool_list(lista):
    val_ini = lista[0]
    lista_bool = []
    for i in range(1, len(lista)):
        if val_ini[0] - 1 == list[i][0] and val_ini[1] - 1 == lista[i][1]:
            lista_bool.append(1)
        else:
            lista_bool.append(0)
        val_ini = lista[i]
    return lista_bool

def alineamiento2(lista, cadena1, cadena2):
    cadena_corta = ""
    cadena_larga = ""
    if len(cadena1) > len(cadena2):
        cadena_corta = cadena2
        cadena_larga = cadena1
    else:
        cadena_corta = cadena1
        cadena_larga = cadena2
    lista_tmp = [i for i in reversed(lista)]
    cadena_retornar = ""
    i = 0
    n = 0
    while i < len(cadena_larga):
        if lista_tmp[i] == 1:
            cadena_retornar += cadena_corta[n]
            n += 1
        else:
            cadena_retornar += "-"
        i += 1
    return cadena_retornar

def obtener_complemento_reverso(secuencia):
    complemento = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complemento_reverso = ''.join(complemento[base] for base in reversed(secuencia))
    return complemento_reverso

def obtener_secuencia_consenso(secuencias):
    secuencia_consenso = ''
    for secuencia in secuencias:
        complemento_reverso = obtener_complemento_reverso(secuencia)
        secuencia_consenso += max(secuencia, complemento_reverso, key=len)
    return secuencia_consenso

def encontrar_camino_hamiltoniano(grafo):
    def backtrack(actual):
        if len(camino) == num_nodos:
            return True
        for vecino in grafo.neighbors(actual):  
            if vecino not in visitados:
                camino.append(vecino)
                visitados.add(vecino)
                if backtrack(vecino):
                    return True
                camino.pop()
                visitados.remove(vecino)
        return False

    num_nodos = len(grafo)
    visitados = set()
    camino = []

    # Verificar si el grafo tiene nodos antes de intentar acceder al primero
    if num_nodos > 0:
        inicio = list(grafo.nodes())[0]
        camino.append(inicio)
        visitados.add(inicio)
    else:
        return None

    # Buscar el camino hamiltoniano
    if backtrack(inicio):
        return camino
    else:
        return None
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def score_(cadena1, cadena2):
    if len(cadena2) < len(cadena1):
        cadena1, cadena2 = cadena2, cadena1
    m, n = len(cadena1), len(cadena2)
    matriz = np.zeros((n, m), int)
    for i in range(n):
        matriz[i][0] = -2 * i
    for j in range(m):
        matriz[0][j] = -2 * j

    for i in range(1, n):
        for j in range(1, m):
            match = matriz[i-1][j-1] + (1 if cadena1[j] == cadena2[i] else -1)
            delete = matriz[i-1][j] - 2
            insert = matriz[i][j-1] - 2
            matriz[i][j] = max(match, delete, insert)
    return matriz[-1][-1]

def alineamiento(matrix):
    tam_x, tam_y = matrix.shape
    for i in range(1, tam_x):
        for j in range(1, tam_y):
            matrix[i][j] = score_(lista_cadenas[i], lista_cadenas[j])
    return matrix

cadena1 = "ATCCGTTGAAGCCGCGGGC"
cadena2 = "TTAACTCGAGG"
cadena3 = "TTAAGTACTGCCCG"
cadena4 = "ATCTGTGTCGGG"
cadena5 = "CGACTCCCGACACA"
cadena6 = "CACAGATCCGTTGAAGCCGCGGG"
cadena7 = "CTCGAGTTAAGTA"
cadena8 = "CGCGGGCAGTACTT"
lista_cadenas = [cadena1, cadena2, cadena3, cadena4, cadena5, cadena6, cadena7, cadena8]

# Obtener la secuencia de consenso
secuencia_consenso = "".join(max(cadena, cadena[::-1], key=len) for cadena in lista_cadenas)
print("Secuencia de consenso:", secuencia_consenso)

# Crear la matriz para el alineamiento
matriz = np.zeros((len(lista_cadenas), len(lista_cadenas)), int)
for i in range(len(lista_cadenas)):
    for j in range(len(lista_cadenas)):
        matriz[j][i] = score_(lista_cadenas[i], lista_cadenas[j])

# Ejecutar el alineamiento
matriz_resultante = alineamiento(matriz)

# Imprimir el score
print("Score del alineamiento:", matriz_resultante[-1][-1])

# Imprimir la matriz resultante
print("Matriz resultante:")
print(matriz_resultante)
