import time

def fib_benchmark():
    N = 100000000  # Note: 100 Million (10x LESS than C++/Julia so it doesn't take all day!)
    a = 0
    b = 1

    start = time.time()
    for _ in range(N):
        next_val = a + b
        a = b
        b = next_val
    end = time.time()

    print(f"Python Result: {a}")
    # Multiply the time by 10 to estimate how long 1 Billion would take
    print(f"Python Time (scaled to 1B): {(end - start) * 10:.4f} seconds")

fib_benchmark()
