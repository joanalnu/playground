import time
import numpy as np

def estimate_pi(n, batch_size=10_000_000):
    inside_circle = 0
    # Process in batches to avoid high RAM usage on large n (e.g., n = 10^9)
    for i in range(0, n, batch_size):
        current_batch = min(batch_size, n-i)

        # Generate random (x, y) coordinates for the batch
        x = np.random.random(current_batch)
        y = np.random.random(current_batch)

        # Vectorised check: (x^2 + y^2 <= 1.0) returns a boolean array
        # np.count_nonzero counts how many coordinates lie inside
        inside_circle += np.count_nonzero(x**2 + y**2 <= 1.0)

    return 4.0 * inside_circle / n

#iterations = 1_000_000_000
iterations = int(input())

print("Running Monte Carlo in Python...")
start_time = time.time()
result = estimate_pi(iterations)
end_time = time.time()

print("-----------------------------------")
print(f"Estimated Pi: {result}")
print(f"Python Execution time: {end_time - start_time:.4f} seconds")
print("-----------------------------------")
