#include <iostream>
#include <vector>
#include <random>

using namespace std;

int main() {
    int n = 100;

    // Random number generator
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dist(1, 100); // Random integers from 1 to 100

    // Create n x n matrix
    vector<vector<int>> matrix(n, vector<int>(n));

    // Fill matrix with random values
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matrix[i][j] = dist(gen);
        }
    }

    // Print the matrix
    for (const auto &row : matrix) {
        for (int x : row)
            cout << x << " ";
        cout << '\n';
    }

    return 0;
}
