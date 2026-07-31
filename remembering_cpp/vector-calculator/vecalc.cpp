#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

void print_vector(const vector<int>& v) {
    cout << "[";
    for (size_t i = 0; i < v.size(); i++) {
        cout << v[i] << (i < v.size() - 1 ? ", " : "");
    }
    cout << "]";
}

vector<int> scalar_mult() {
    int n, scalar;
    cout << "\nEnter the size of the vector: ";
    cin >> n;

    vector<int> v1(n);
    cout << "Enter " << n << " elements for the vector (separated by space): ";
    for (int i = 0; i < n; i++) {
        cin >> v1[i];
    }

    cout << "Enter the scalar: ";
    cin >> scalar;
    
    vector<int> v3(n);
    for (int i = 0; i < n; i++) {
        v3[i] = v1[i] * scalar;
    }

    return v3;
}

long long dot_prod() {
    int n;
    long long sum=0; // just in case it gets large
    cout << "\nEnter the size of the vectors: ";
    cin >> n;

    vector<int> v1(n), v2(n);
    cout << "Enter " << n << " elements for the first vector (separated by space): ";
    for (int i=0; i<n; i++) cin >> v1[i];

    cout << "Enter " << n << " elements for the second vector (separated by space): ";
    for (int i=0; i<n; i++) cin >> v2[i];

    for (int i=0; i<n; i++) {
        sum += v1[i] * v2[i];
    }

    return sum;
}

vector<int> cross_prod() {
    cout << "\nThe vectors must be 3D.\n";
    vector<int> v1(3), v2(3);
    
    cout << "Enter 3 elements for the first vector: ";
    for (int i = 0; i < 3; i++) cin >> v1[i];
    
    cout << "Enter 3 elements for the second vector: ";
    for (int i = 0; i < 3; i++) cin >> v2[i];

    vector<int> v3(3);

    // from 0 not from 1, because although indices are (1,2,3), C++ uses 0-based indexing for the vectors
    for (int i = 0; i < 3; i++) {
        v3[i] = (v1[(i+1)%3] * v2[(i+2)%3]) - (v1[(i+2)%3] * v2[(i+1)%3]);
    }

    return v3;
}

double norm() {
    cout << "\nUsing the p-norm\n";

    int p, n;
    cout << "Enter the size of the vector: ";
    cin >> n;

    vector<int> v(n);
    cout << "Enter p (natural number): ";
    cin >> p;
    
    cout << "Enter " << n << " elements for the vector: ";
    for (int i = 0; i < n; i++) cin >> v[i];

    double sum = 0; // Use double to prevent overflow and allow precise math
    for (int i = 0; i < n; i++) {
        sum += pow(v[i], p); 
    }

    return pow(sum, 1.0 / p); 
}

int main() {
    string op;
    cout << "Operator (scalar, dot, cross, norm): ";
    cin >> op;

    if (op == "scalar") {
        vector<int> result = scalar_mult();
        cout << "\nResult: ";
        print_vector(result);
        cout << endl;
    }
    else if (op =="dot") {
        long long res = dot_prod();
        cout << "\n Result: " << res << endl;
    }
    else if (op == "cross") {
        vector<int> result = cross_prod();
        cout << "\nResult: ";
        print_vector(result);
        cout << endl;
    } 
    else if (op == "norm") {
        cout << "\nResult: " << norm() << endl;
    } 
    else {
        cout << "\nOperator not valid." << endl;
    }

    return 0;
}
