#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include "LimpiadorArchivo.h"
using namespace std;

const int PENALIZACION_HUECO = -2;
const int PUNTAJE_COINCIDENCIA = 1;
const int PUNTAJE_NO_COINCIDENCIA = -1;

struct Celda {
    int puntaje;
    char direccion;
};

void exportarSecuencia(const string& secuencia, const string& nombre_archivo) {
    ofstream archivo(nombre_archivo);
    if (archivo.is_open()) {
        for (int i = 0; i < secuencia.length(); ++i) {
            archivo << i << "\t" << secuencia[i] << endl;
        }
        archivo.close();
        cout << "Secuencia exportada correctamente como '" << nombre_archivo << "'" << endl;
    }
    else {
        cerr << "Error al abrir el archivo para exportar la secuencia" << endl;
    }
}

tuple<int, map<string, map<string, int>>, pair<string, string>, int> needlemanWunsch(const string& secuencia1, const string& secuencia2) {
    int m = secuencia1.length();
    int n = secuencia2.length();

    // Inicialización de la matriz
    map<string, map<string, int>> dp;
    dp[""][secuencia2] = 0;
    for (int i = 1; i <= m; ++i) {
        dp[secuencia1.substr(0, i)][""] = i * PENALIZACION_HUECO;
    }
    for (int j = 1; j <= n; ++j) {
        dp[""][secuencia2.substr(0, j)] = j * PENALIZACION_HUECO;
    }

    // Llenado de la matriz
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            int coincidencia = (secuencia1[i - 1] == secuencia2[j - 1]) ? PUNTAJE_COINCIDENCIA : PUNTAJE_NO_COINCIDENCIA;
            int puntaje_diagonal = dp[secuencia1.substr(0, i - 1)][secuencia2.substr(0, j - 1)] + coincidencia;
            int puntaje_arriba = dp[secuencia1.substr(0, i - 1)][secuencia2.substr(0, j)] + PENALIZACION_HUECO;
            int puntaje_izquierda = dp[secuencia1.substr(0, i)][secuencia2.substr(0, j - 1)] + PENALIZACION_HUECO;

            int max_puntaje = max(puntaje_diagonal, max(puntaje_arriba, puntaje_izquierda));

            dp[secuencia1.substr(0, i)][secuencia2.substr(0, j)] = max_puntaje;
        }
    }

    // Encontrar el score
    int score = dp[secuencia1][secuencia2];

    // Realizar el traceback para encontrar las secuencias alineadas y el número de rupturas
    string alineamiento_secuencia1 = "";
    string alineamiento_secuencia2 = "";
    int rupturas = 0;
    int i = m;
    int j = n;
    while (i > 0 || j > 0) {
        int puntaje_actual = dp[secuencia1.substr(0, i)][secuencia2.substr(0, j)];
        if (i > 0 && j > 0 && puntaje_actual == dp[secuencia1.substr(0, i - 1)][secuencia2.substr(0, j - 1)] + ((secuencia1[i - 1] == secuencia2[j - 1]) ? PUNTAJE_COINCIDENCIA : PUNTAJE_NO_COINCIDENCIA)) {
            alineamiento_secuencia1 = secuencia1[i - 1] + alineamiento_secuencia1;
            alineamiento_secuencia2 = secuencia2[j - 1] + alineamiento_secuencia2;
            --i;
            --j;
        }
        else if (i > 0 && puntaje_actual == dp[secuencia1.substr(0, i - 1)][secuencia2.substr(0, j)] + PENALIZACION_HUECO) {
            alineamiento_secuencia1 = secuencia1[i - 1] + alineamiento_secuencia1;
            alineamiento_secuencia2 = '-' + alineamiento_secuencia2;
            --i;
            ++rupturas;  // Incrementar rupturas cuando hay un gap en secuencia2
        }
        else {
            alineamiento_secuencia1 = '-' + alineamiento_secuencia1;
            alineamiento_secuencia2 = secuencia2[j - 1] + alineamiento_secuencia2;
            --j;
            ++rupturas;  // Incrementar rupturas cuando hay un gap en secuencia1
        }
    }

    // Exportar la secuencia de salida
    exportarSecuencia(alineamiento_secuencia1, "secuencia_salida.txt");

    return make_tuple(score, dp, make_pair(alineamiento_secuencia1, alineamiento_secuencia2), rupturas);
}

int main()
{
    //Parte1
    /*
    string secuencia1 = "AAAC";
    string secuencia2 = "AGC";
    */
    //parte2
    cout << "COV Y influencia" << endl;
    string secuencia1 = leerSecuenciaBacteria(1000);
    string secuencia2 = leerSecuenciaInfluencia(1000);
    int score;
    map<string, map<string, int>> matriz_puntuacion;
    pair<string, string> alineamiento;
    int rupturas;
    tie(score, matriz_puntuacion, alineamiento, rupturas) = needlemanWunsch(secuencia1, secuencia2);
    cout << "Score obtenido: " << score << endl;
    cout << "Número de rupturas: " << rupturas << endl;
    // Mostrar el alineamiento
    cout << "Alineamiento:" << endl;
    cout << alineamiento.first << endl;
    cout << alineamiento.second << endl;

    return 0;
}