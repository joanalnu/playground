#include <iostream>
#include <chrono>

int main() {
    long long n = 10000000000000000; // size of the square matrix being computed

    auto start_time = std::chrono::high_resolution_clock::now();

    // nested loop increases complexity!
    for (long long i=0; i<n; ++i) {
        for (long long j=0; j<n; ++j) {
            for (long long k=0; k<n; ++k) {
                for (long long m=0; m<n; ++m) {
                    long long q = i * j * k * m;
                }
            }
        }
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;

    std::cout << "Matrix size : " << n << "^4" << std::endl;
    std::cout << "Time Elapsed : " << elapsed.count() << " seconds" << std::endl;

    return 0;
}
