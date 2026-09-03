#include <iostream>
using namespace std;

bool isprime(long long n) {
    if (n < 2) return false;

    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    long long n;
    cin >> n;

    long long largest_factor = 0;

    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0 && isprime(i)) {
            largest_factor = i;
        }
    }

    // n itself might be prime
    if (largest_factor == 0 && isprime(n)) {
        largest_factor = n;
    }

    cout << "Largest prime factor of " << n << " is " << largest_factor << endl;

    return 0;
}

