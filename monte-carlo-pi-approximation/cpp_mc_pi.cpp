#include <iostream>
#include <random>
#include <chrono>
using namespace std;

int estimate_pi(long long total_points) {
  long long inside_circle = 0;

  // Set up a high-quality random number generator
  random_device rd;
  mt19937 generator(rd());
  uniform_real_distribution<double> distribution(0.0, 1.0);

  // Run the Monte Carlo simulation
  for (long long i = 0; i < total_points; i++) {
    double x = distribution(generator);
    double y = distribution(generator);

    // If the point is inside the unit circle
    if (x * x + y * y <= 1.0) {
      inside_circle++;
    }
  }

  return 4.0 * inside_circle / total_points;
}

int main() {
    // 100 millian iteratioong
    long total_points = 1000000000;
    cin >> total_points;

    std::cout << "Running Monte Carlo in C++" << std::endl;

    // execute the sequence
    auto start_time = std::chrono::high_resolution_clock::now();
    long long pi_estimate = estimate_pi(total_points);
    auto end_time = std::chrono::high_resolution_clock::now();

    // calculate the time
    std::chrono::duration<double, std::milli> elapsed = end_time - start_time;

    // Output results
    std::cout << "-----------------------------------" << std::endl;
    std::cout << "Estimated Pi: " << pi_estimate << std::endl;
    std::cout << "C++ Execution time: " << elapsed.count() << "ms (" << elapsed.count() / 1000.0 << " seconds)" << std::endl;
    std::cout << "-----------------------------------" << std::endl;

    return 0;
}
