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

num_ca = 0


def convert(list):
  return tuple(i for i in list)


def recorrer_matrix(matrix, x, y):
  if (x == 0 and y != 0):
    G.add_edge((x, y), (x, y - 1), weight=-1)
    recorrer_matrix(matrix, x, y - 1)
  if (y == 0 and x != 0):
    G.add_edge((x, y), (x - 1, y), weight=-1)
    recorrer_matrix(matrix, x - 1, y)
  if (x == 0 and y == 0 or (x - 1 < 0 or y - 1 < 0)):
    return 0

  tam = len(matrix[x - 1][y - 1])
  for i in range(1, tam):
    recorrer_matrix(matrix, matrix[x - 1][y - 1][i][0],
                    matrix[x - 1][y - 1][i][1])
    G.add_edge((x, y), convert(matrix[x - 1][y - 1][i]), weight=1)


def alineamiento(matrix):
  tam_x = len(matrix)
  tam_y = len(matrix[0])
  recorrer_matrix(matrix, tam_x, tam_y)
  nx.draw(G, with_labels=True)
  plt.savefig("generador.png")


def swap_(cadena1, cadena2):
  temp = cadena1
  cadena1 = cadena2
  cadena2 = temp
  return cadena1, cadena2


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
      if (lista_cam[i][j] == lista_cam[i][j + 1] + 1
          or lista_cam[i][j] == lista_cam[i][j + 1] - 1):
        lista_temp += cadena_temp[temp_indice]
        temp_indice -= 1

      else:
        lista_temp += '-'
    lista2.append(lista_temp[::-1])
    temp_indice = len(cadena_temp) - 1
    lista_temp = ''
  return lista2


def bool_list(list):
  val_ini = list[0]
  lista_bool = []
  for i in range(1, len(list)):
    if (val_ini[0] - 1 == list[i][0] and val_ini[1] - 1 == list[i][1]):
      lista_bool.append(1)
    else:
      lista_bool.append(0)
    val_ini = list[i]
  return lista_bool


def alineamiento2(lista, cadena1, cadena2):
  cadena_corta = ""
  cadena_larga = ""
  if (len(cadena1) > len(cadena2)):
    cadena_corta = cadena2
    cadena_larga = cadena1
  else:
    cadena_corta = cadena1
    cadena_larga = cadena2
  lista_tmp = [i for i in reversed(lista)]
  cadena_retornar = ""
  i = 0
  n = 0
  while (i < len(cadena_larga)):
    if (lista_tmp[i] == 1):
      cadena_retornar += cadena_corta[n]
      n += 1
    else:
      cadena_retornar += "-"
    i += 1
  return cadena_retornar


def alineamiento(matrix):
  tam_x = len(matrix)
  tam_y = len(matrix[0])
  recorrer_matrix(matrix, tam_x, tam_y)
  nx.draw(G, with_labels=True)
  plt.savefig("generador.png")


def score_(cadena1, cadena2):
  if len(cadena2) < len(cadena1):
    cadena1, cadena2 = swap_(cadena1, cadena2)
  lista = []
  m, n = len(cadena1), len(cadena2)
  matriz = np.zeros((len(cadena2), len(cadena1)), int)
  lleno = 0

  for i in range(0, n):
    matriz[i][0] = lleno
    lleno = lleno - 2

  lleno = 0
  for j in range(0, m):
    matriz[0][j] = lleno
    lleno = lleno - 2

  lista_caminos = []
  random_ = 0
  for i in range(1, n):
    lista_temp4 = []
    for j in range(1, m):
      lista_temp = []
      matriz[i][j], lista_temp = maximo(matriz, i, j, cadena1, cadena2)
  score = matriz[n - 1][m - 1]
  return score


def global_(cadena1, cadena2):

  if len(cadena2) < len(cadena1):
    cadena1, cadena2 = swap_(cadena1, cadena2)

  lista = []
  m, n = len(cadena1), len(cadena2)
  matriz = np.zeros((len(cadena2), len(cadena1)), int)
  lleno = 0

  for i in range(0, n):
    matriz[i][0] = lleno
    lleno = lleno - 2

  lleno = 0
  for j in range(0, m):
    matriz[0][j] = lleno
    lleno = lleno - 2

  lista_caminos = []
  random_ = 0
  for i in range(1, n):
    lista_temp4 = []
    for j in range(1, m):
      lista_temp = []
      lista_temp2 = []
      lista_temp3 = []

      matriz[i][j], lista_temp = maximo(matriz, i, j, cadena1, cadena2)
      lista_temp3.append(matriz[i][j])
      lista_temp3 += (lista_temp)
      lista_temp4.append(lista_temp3)
    lista_caminos.append(lista_temp4)
  alineamiento(lista_caminos)
  lista = [e for e in G.edges]
  lista2 = [i for i in reversed(lista)]
  val_ini = lista2[0][0]
  tree = Tree()
  duplicado = 0

  lista_graph = []

  for path in nx.all_simple_paths(G, source=(n - 1, m - 1), target=(0, 0)):
    lista_graph.append(path)

  lst = [list(row) for row in lista_graph]

  lista_alineamientos = []

  lista_alineamientos_temp1 = []
  lista_alineamientos_temp = []
  for j in range(0, len(lista_graph[0])):
    tup1 = lista_graph[0][j]
    indicei = tup1[0]
    indicej = tup1[1]
    indice = matriz[indicei][indicej]
    lista_alineamientos_temp.append(indice)
  lista_alineamientos.append(lista_alineamientos_temp)
  lista1 = []
  lista2 = []
  score_ = []
  alineamientos_ = []

  cadena_temp = cadena2[1:]
  for i in range(0, len(lista_alineamientos)):

    lista1.append(cadena_temp)
  score = matriz[n - 1][m - 1]
  score_.append(str(score))
  lista2 = alineamientosfun(lista_alineamientos, lista2, cadena2, cadena1)

  alineamientos = matriz[n - 1][m - 1]
  alineamientos_.append(str(len(lista_alineamientos)))
  return lista1[0], lista2[0]


def matriz_scores(lista_cadenas, matrizscores, tamaño):
  for i in range(0, tamaño):
    for j in range(i + 1, tamaño):
      matrizscores[i][j] = matrizscores[j][i] = score_(lista_cadenas[i],
                                                       lista_cadenas[j])

  return matrizscores


def score_maximo_matriz(matrizscores, tamaño):
  suma_linea = 0
  linea_a_usar = 0
  for i in range(0, tamaño):
    suma_linea = 0
    for j in range(0, tamaño):
      suma_linea += matrizscores[i][j]
    if i == 0:
      maximo = suma_linea
      linea_a_usar = i
    if suma_linea > maximo:
      maximo = suma_linea
      linea_a_usar = i
  return maximo, linea_a_usar


def alineamiento_por_pares(cadena_mayor, lista_cadenas):
  alin_temp1 = []
  alin_temp2 = []
  list_alin_pares = []
  for i in range(0, len(lista_cadenas)):
    alin_temp1, alin_temp2 = global_(cadena_mayor, lista_cadenas[i])

    list_alin_pares.append(alin_temp2)
    if i == 0:
      list_alin_pares.append(alin_temp1)

  return list_alin_pares


def completar_alin_pares(list_alin_pares):
  maximo = 0
  lon_temp = 0
  gap = "-"
  for i in range(0, len(list_alin_pares)):
    lon_temp = len(list_alin_pares[i])
    if maximo < lon_temp:
      maximo = lon_temp
  falta_temp = 0
  for j in range(0, len(list_alin_pares)):
    while len(list_alin_pares[j]) < maximo:
      list_alin_pares[j] += gap

  return list_alin_pares


cadena1 = "ATCCGTTGAAGCCGCGGGC"
cadena2 = "TTAACTCGAGG"
cadena3 = "TTAAGTACTGCCCG"
cadena4 = "ATCTGTGTCGGG"
cadena5 = "CGACTCCCGACACA"
cadena6 = "CACAGATCCGTTGAAGCCGCGGG"
cadena7 = "CTCGAGTTAAGTA"
cadena8 = "CGCGGGCAGTACTT"
lista_cadenas = []
lista_cadenas.append(cadena1)
lista_cadenas.append(cadena2)
lista_cadenas.append(cadena3)
lista_cadenas.append(cadena4)
lista_cadenas.append(cadena5)
lista_cadenas.append(cadena6)
lista_cadenas.append(cadena7)
lista_cadenas.append(cadena8)
tamaño = len(lista_cadenas)
matrizscores = np.zeros((tamaño, tamaño), int)
print(lista_cadenas)
matriz_scores(lista_cadenas, matrizscores, tamaño)
print(matrizscores)
score_a_usar, cadena_a_usar = score_maximo_matriz(matrizscores, tamaño)
cadena_manda = lista_cadenas[cadena_a_usar]
print("el score a usar de la matriz es ", score_a_usar, "siendo de la cadena",
      cadena_manda)
indice_a_eliminar = lista_cadenas.index(cadena_manda)
print("esta en el indice", indice_a_eliminar)
lista_cadenas.pop(indice_a_eliminar)
print("las demas cadenas son", lista_cadenas)

caminos_pares_final = alineamiento_por_pares(cadena_manda, lista_cadenas)
print(caminos_pares_final)
caminos_pares_final = completar_alin_pares(caminos_pares_final)
print(caminos_pares_final)

np.savetxt('resultado.txt', matrizscores, fmt='%.2f')
file1 = open("resultado.txt", "a")
file1.write("\n")

for i in range(0, len(caminos_pares_final)):
  for j in range(0, len(caminos_pares_final[0])):
    file1.writelines(caminos_pares_final[i][j])

  file1.write(" ")

file1.write("\n")
