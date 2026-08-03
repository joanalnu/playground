#include <iostream>
#include <random>
#include <chrono>

int main() {
    // 100 millian iterations
    const long long total_points = 1000000000;
    long long inside_circle = 0;

    // Set up a high-quality random number generator
    std::random_device rd;
    std::mt19937 generator(rd());
    std::uniform_real_distribution<double> distribution(0.0, 1.0);

    std::cout << "Running Monte Carlo in C++" << std::endl;

    // 1. START THE STOPWATCH
    auto start_time = std::chrono::high_resolution_clock::now();

    // Run the Monte Carlo simulation
    for (long long i = 0; i < total_points; ++i) {
        double x = distribution(generator);
        double y = distribution(generator);

        // If the point is inside the unit circle
        if (x * x + y * y <= 1.0) {
            inside_circle++;
        }
    }

    // 2. STOP THE STOPWATCH
    auto end_time = std::chrono::high_resolution_clock::now();

    // 3. CALCULATE THE DIFFERENCE
    // We cast the duration into milliseconds using double precision
    std::chrono::duration<double, std::milli> elapsed = end_time - start_time;

    // Calculate Pi
    double pi_estimate = 4.0 * inside_circle / total_points;

    // Output results
    std::cout << "-----------------------------------" << std::endl;
    std::cout << "Estimated Pi: " << pi_estimate << std::endl;
    std::cout << "C++ Execution time: " << elapsed.count() << "ms (" << elapsed.count() / 1000.0 << " seconds)" << std::endl;
    std::cout << "-----------------------------------" << std::endl;

    return 0;
}
