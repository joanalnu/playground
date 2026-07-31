#include <iostream>
#include <chrono>

int main() {
    const int N = 1000000000; // 1 Billion
    unsigned long long a = 0;
    unsigned long long b = 1;

    auto start = std::chrono::high_resolution_clock::now();
    
    for (int i = 0; i < N; ++i) {
        unsigned long long next = a + b;
        a = b;
        b = next;
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    std::cout << "C++ Result: " << a << std::endl;
    std::cout << "C++ Time : " << elapsed.count() << " seconds" << std::endl;

    return 0;
}

