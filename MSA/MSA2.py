from Bio.Align import PairwiseAligner


def alineamiento_por_pares(seq1, seq2):
    alineador = PairwiseAligner()
    alineamientos = alineador.align(seq1, seq2)
    mejor_alineamiento = alineamientos[0]
    puntaje_alineamiento = mejor_alineamiento.score
    secuencia_alineada1 = mejor_alineamiento.aligned[0]
    secuencia_alineada2 = mejor_alineamiento.aligned[1]
    return secuencia_alineada1, secuencia_alineada2, puntaje_alineamiento


def alineamiento_estrella(secuencias):
    """
    Realiza el Alineamiento Múltiple de Secuencias utilizando el método de Alineamiento Estrella.
    """
    # Inicializa el alineamiento con la primera secuencia
    alineamiento = secuencias[0]
    # Itera a través de las secuencias restantes
    for seq in secuencias[1:]:
        mejor_puntaje = float('-inf')
        mejor_alineamiento = None
        # Encuentra la mejor posición para insertar la secuencia
        for i in range(len(alineamiento) + 1):
            alineamiento_temporal = alineamiento[:i] + seq + alineamiento[i:]
            suma_puntajes = 0
            # Calcula el puntaje de alineamiento con cada secuencia en el alineamiento
            for secuencia_alineada in alineamiento:
                _, _, puntaje = alineamiento_por_pares(alineamiento_temporal, secuencia_alineada)
                suma_puntajes += puntaje
            # Actualiza el mejor alineamiento si el puntaje actual es mayor
            if suma_puntajes > mejor_puntaje:
                mejor_puntaje = suma_puntajes
                mejor_alineamiento = alineamiento_temporal
        # Actualiza el alineamiento final con el mejor alineamiento encontrado
        alineamiento = mejor_alineamiento
    return alineamiento, mejor_puntaje


# Secuencias BRCA1
secuencias_directas = [
    "TGCCGGCAGGGATGTGCTTG",
    "GTTTAGGTTTTTGCTTATGCAGCATCCA",
    "GGAAAAGCACAGAACTGGCCAACA",
    "GCCAGTTGGTTGATTTCCACCTCCA",
    "ACCCCCGACATGCAGAAGCTG",
    "TGACGTGTCTGCTCCACTTCCA"
]

secuencias_reversas = [
    "TGCTTGCAGTTTGCTTTCACTGATGGA",
    "TCAGGTACCCTGACCTTCTCTGAAC",
    "GTGGGTTGTAAAGGTCCCAAATGGT",
    "TGCCTTGGGTCCCTCTGACTGG",
    "GTGGTGCATTGATGGAAGGAAGCA",
    "AGTGAGAGGAGCTCCCAGGGC"
]

# Alineamiento de secuencias directas
alineamientos_directas, puntaje_directas = alineamiento_estrella(secuencias_directas)

# Alineamiento de secuencias reversas
alineamientos_reversas, puntaje_reversas = alineamiento_estrella(secuencias_reversas)

# Alineamiento de todas las secuencias juntas
alineamiento_final_todas, puntaje_final_todas = alineamiento_estrella(secuencias_directas + secuencias_reversas)

# Dividir el alineamiento final en secuencias directas y reversas
alineamiento_final_directas_todas = alineamiento_final_todas[:len(secuencias_directas)]
alineamiento_final_reversas_todas = alineamiento_final_todas[len(secuencias_directas):]

# Comparar los alineamientos de secuencias directas y reversas
for i, (seq_directa, seq_reversa) in enumerate(zip(alineamiento_final_directas_todas, alineamiento_final_reversas_todas)):
    print(f"Comparación para la muestra {chr(65 + i)}:")
    print("Secuencia directa:", seq_directa)
    print("Secuencia reversa:", seq_reversa)
    print("Coinciden:" if seq_directa == seq_reversa else "No coinciden")
    print()

# Imprimir resultados
print("Secuencia Final (Directas):")
print(' '.join(alineamientos_directas))
print("Puntaje (Directas):", puntaje_directas)
print()
print("Secuencia Final (Reversas):")
print(' '.join(alineamientos_reversas))
print("Puntaje (Reversas):", puntaje_reversas)
print()
print("Secuencia Final (Todas):")
print(' '.join(alineamiento_final_todas))
print("Puntaje (Todas):", puntaje_final_todas)
