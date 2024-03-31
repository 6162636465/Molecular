#include <iostream>
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

tuple<int, map<string, map<string, int>>, pair<string, string>> needlemanWunsch(const string& secuencia1, const string& secuencia2) {
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

    // Realizar el traceback para encontrar las secuencias alineadas
    string alineamiento_secuencia1 = "";
    string alineamiento_secuencia2 = "";
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
        }
        else {
            alineamiento_secuencia1 = '-' + alineamiento_secuencia1;
            alineamiento_secuencia2 = secuencia2[j - 1] + alineamiento_secuencia2;
            --j;
        }
    }

    return make_tuple(score, dp, make_pair(alineamiento_secuencia1, alineamiento_secuencia2));
}

int main() 
{   
    //Parte1
    /*
    string secuencia1 = "AAAC";
    string secuencia2 = "AGC";
    */
    //parte2
    cout << "COV Y BACTERIA" << endl;
    string secuencia1 = leerSecuenciaCov(1000);
    string secuencia2 = leerSecuenciaBacteria(1000);
    int score;
    map<string, map<string, int>> matriz_puntuacion;
    pair<string, string> alineamiento;
    tie(score, matriz_puntuacion, alineamiento) = needlemanWunsch(secuencia1, secuencia2);
    cout << "Score obtenido: " << score << endl;
    // Mostrar la matriz de puntuación
    /*
    for (auto& fila : matriz_puntuacion) {
        for (auto& valor : fila.second) {
            cout << valor.second << "\t";
        }
        cout << endl;
    }*/
    // Mostrar el alineamiento
    cout << "Alineamiento:" << endl;
    cout << alineamiento.first << endl;
    cout << alineamiento.second << endl;

    cout << "COV Y influencia" << endl;
    string secuencia3 = leerSecuenciaCov(1000);
    string secuencia4 = leerSecuenciaInfluencia(1000);
    int score1;
    map<string, map<string, int>> matriz_puntuacion1;
    pair<string, string> alineamiento1;
    tie(score1, matriz_puntuacion1, alineamiento1) = needlemanWunsch(secuencia3, secuencia4);
    cout << "Score obtenido: " << score << endl;
    cout << "Alineamiento:" << endl;
    cout << alineamiento1.first << endl;
    cout << alineamiento1.second << endl;

    cout << "influencia Y BACTERIA" << endl;
    string secuencia5 = leerSecuenciaInfluencia(1000);
    string secuencia6 = leerSecuenciaBacteria(1000);
    int score2;
    map<string, map<string, int>> matriz_puntuacion2;
    pair<string, string> alineamiento2;
    tie(score2, matriz_puntuacion2, alineamiento2) = needlemanWunsch(secuencia5, secuencia6);
    cout << "Score obtenido: " << score << endl;
    cout << "Alineamiento:" << endl;
    cout << alineamiento2.first << endl;
    cout << alineamiento2.second << endl;

    return 0;
}
