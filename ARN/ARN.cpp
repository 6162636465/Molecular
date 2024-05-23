#include <iostream>
#include <vector>
#include <string>
#include <functional>
#include <iomanip>

// Función para calcular la energía entre dos nucleótidos
int energy1(char a, char b) {
    if ((a == 'C' && b == 'G') || (a == 'G' && b == 'C')) return -1;
    if ((a == 'A' && b == 'U') || (a == 'U' && b == 'A')) return -1;

    return 0;
}

int energy2(char a, char b) {
    if ((a == 'C' && b == 'G') || (a == 'G' && b == 'C')) return -1;
    if ((a == 'A' && b == 'U') || (a == 'U' && b == 'A')) return -1;
    if ((a == 'C' && b == 'G') || (a == 'G' && b == 'C')) return -5;
    if ((a == 'A' && b == 'U') || (a == 'U' && b == 'A')) return -4;
    if ((a == 'G' && b == 'U') || (a == 'U' && b == 'G')) return -1;
    return 0;
}

// Función para imprimir la matriz de energía
void printEnergyMatrix(const std::vector<std::vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int val : row) {
            if (val < 0) {
                std::cout << std::setw(4) << val << ' ';
            }
            else {
                std::cout << "  " << '-';
            }
        }
        std::cout << std::endl;
    }
}

// Función para imprimir la matriz de nucleótidos
void printNucleotides(const std::string& rna, int i, int j) {
    for (int idx = i; idx <= j; ++idx) {
        if (idx == i || idx == j) {
            std::cout << rna[idx];
        }
        else {
            std::cout << '-';
        }
    }
}

// Función para calcular la estructura secundaria del ARN usando programación dinámica
std::string secondaryStructure(const std::string& rna, bool useEnergy1 = true) {
    int n = rna.size();
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
    std::vector<std::vector<int>> traceback(n, std::vector<int>(n, -1));

    // Seleccionar la función de energía a usar
    auto energy = useEnergy1 ? energy1 : energy2;

    // Llenar la tabla dp
    for (int length = 1; length < n; ++length) {
        for (int i = 0; i + length < n; ++i) {
            int j = i + length;
            dp[i][j] = dp[i][j - 1];
            traceback[i][j] = j - 1;

            for (int k = i; k < j; ++k) {
                int currentEnergy = dp[i][k] + dp[k + 1][j - 1] + energy(rna[k], rna[j]);
                if (currentEnergy < dp[i][j]) {
                    dp[i][j] = currentEnergy;
                    traceback[i][j] = k;
                }
            }
        }
    }

    // Imprimir la matriz de energía
    std::cout << "Matriz de Energía:\n";
    printEnergyMatrix(dp);

    // Reconstruir la estructura secundaria
    std::string structure(n, '.');
    std::function<void(int, int)> reconstruct = [&](int i, int j) {
        if (i >= j) return;
        int k = traceback[i][j];
        if (k == j - 1) {
            reconstruct(i, k);
        }
        else {
            structure[k] = '(';
            structure[j] = ')';
            reconstruct(i, k);
            reconstruct(k + 1, j - 1);
        }
    };

    reconstruct(0, n - 1);

    std::cout << "Estructura secundaria:\n";
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            if (dp[i][j] >= 0) {
                std::cout << std::setw(2) << dp[i][j] << ' ';
            }
            else {
                std::cout << "-- ";
            }
        }
        std::cout << std::endl;
    }

    std::cout << "Score: " << dp[0][n - 1] << std::endl;

    std::cout << "Estructura secundaria:\n";
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            if (dp[i][j] >= 0) {
                printNucleotides(rna, i, j);
                std::cout << std::endl;
            }
        }
    }

    std::cout << structure << std::endl;

    return structure;
}

int main() {
    std::string rna = "GGAAAUCC";

    // Calcular la estructura secundaria con la primera función de energía
    std::cout << "Usando energía 1:\n";
    std::string structure1 = secondaryStructure(rna, true);


    // Calcular la estructura secundaria con la segunda función de energía
    std::cout << "Usando energía 2:\n";
    std::string structure2 = secondaryStructure(rna, false);

    return 0;
}
