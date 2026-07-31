import random
import time

def estimate_pi(n):
    inside_circle = 0
    for _ in range(n):
        x = random.random()
        y = random.random()

        # check if the coordinate is inside the unit circle
        if x**2 + y**2 <= 1.0:
            inside_circle += 1
    return 4.0 * inside_circle / n

iterations = 20_000_000

print("Running Monte Carlo in Python...")
start_time = time.time()
result = estimate_pi(iterations)
end_time = time.time()

print(f"Result: {result}")
print(f"Python execution time: {end_time - start_time:.4f} seconds")
