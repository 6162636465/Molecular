#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

string leerSecuenciaInfluencia(int contadorPalabras) {
    // Abrir el archivo
    ifstream archivo("SecuenciaInfluecnia.txt");
    if (!archivo.is_open()) {
        cerr << "Error: No se pudo abrir el archivo 'Secuencia.txt'" << endl;
        return "";
    }

    // Leer la secuencia del archivo
    string secuencia;
    string linea;
    while (getline(archivo, linea)) {
        secuencia += linea;
    }

    // Eliminar espacios de la secuencia
    secuencia.erase(remove(secuencia.begin(), secuencia.end(), ' '), secuencia.end());

    // Devolver la subcadena de acuerdo al contador de palabras
    if (contadorPalabras <= secuencia.size()) {
        return secuencia.substr(0, contadorPalabras);
    }
    else {
        cerr << "Error: El contador de palabras excede la longitud de la secuencia." << endl;
        return "";
    }
}
string leerSecuenciaBacteria(int contadorPalabras) {
    // Abrir el archivo
    ifstream archivo("SecuenciaBacteria.txt");
    if (!archivo.is_open()) {
        cerr << "Error: No se pudo abrir el archivo 'Secuencia.txt'" << endl;
        return "";
    }

    // Leer la secuencia del archivo
    string secuencia;
    string linea;
    while (getline(archivo, linea)) {
        secuencia += linea;
    }

    // Eliminar espacios de la secuencia
    secuencia.erase(remove(secuencia.begin(), secuencia.end(), ' '), secuencia.end());

    // Devolver la subcadena de acuerdo al contador de palabras
    if (contadorPalabras <= secuencia.size()) {
        return secuencia.substr(0, contadorPalabras);
    }
    else {
        cerr << "Error: El contador de palabras excede la longitud de la secuencia." << endl;
        return "";
    }
}
string leerSecuenciaCov(int contadorPalabras) {
    // Abrir el archivo
    ifstream archivo("SecuenciaCov.txt");
    if (!archivo.is_open()) {
        cerr << "Error: No se pudo abrir el archivo 'Secuencia.txt'" << endl;
        return "";
    }

    // Leer la secuencia del archivo
    string secuencia;
    string linea;
    while (getline(archivo, linea)) {
        secuencia += linea;
    }

    // Eliminar espacios de la secuencia
    secuencia.erase(remove(secuencia.begin(), secuencia.end(), ' '), secuencia.end());

    // Devolver la subcadena de acuerdo al contador de palabras
    if (contadorPalabras <= secuencia.size()) {
        return secuencia.substr(0, contadorPalabras);
    }
    else {
        cerr << "Error: El contador de palabras excede la longitud de la secuencia." << endl;
        return "";
    }
}