import numpy as np
import matplotlib.pyplot as plt

def visualizar_secuencia(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        datos = f.readlines()
    
    secuencia = [int(line.split('\t')[0]) for line in datos]
    indices = list(range(len(secuencia)))
    
    plt.plot(secuencia, indices, marker='o', color='red', linestyle='None')
    plt.xlabel('Posición en Secuencia de Salida')
    plt.ylabel('Índice')
    plt.title('Secuencia de Salida')
    plt.grid(True)
    plt.show()

# Reemplaza 'secuencia_salida.txt' con el nombre de tu archivo generado por C++
visualizar_secuencia('secuencia_salida.txt')
