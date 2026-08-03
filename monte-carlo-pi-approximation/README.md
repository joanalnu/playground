# Monte Carlo Pi Approximations

# Aim

Compare the execution speeds between `python`, `C++`, and `Julia` by approximation $\pi$ using a standard monte carlo simulation.

# Files
- `python_mc_pi.py`: python script
- `cpp_mc_pi.cpp`: C++ script
- `cpp_mc_pi`: compiled c++ code
- `julia_mc_pi.jl`: julia script
- `ABC_log.txt`: the run output for each language
- `README.md`: this file

# Dependencies

| Language | Python (3.14.6) | C++ (clang++ 21.0.0) | Julia (1.12.6) |
| :--- | :--- | :--- | :--- |
| Random Point Generator | `random` | `random`| `rand()` |
| Time keeping | `time` | `std::chrono::high_resolution_clock` | Benchmarktools `@btime` |

And, of course, you need to have all three languages installed to be able to run the code.

# Results

### Python

```
Running Monte Carlo in Python...
-----------------------------------
Estimated Pi: 3.141605792
Python Execution time: 140.1580 seconds
-----------------------------------
```

_Note: the Python code was executed using both a system-wide and a virtual environment installation, both obtained similar execution times (up to 0.01 order of magnitude)_

### C++

```
Running Monte Carlo in C++
-----------------------------------
Estimated Pi: 3.14155
C++ Execution time: 10056ms (10.056 seconds)
-----------------------------------
``` 

_Note: the code was compiled using the `-O3` tag for optimisation leve 3 (the maximum), which should make the programm run as fast as possible._

### Julia

```
Running Monte Carlo in Julia
-----------------------------------
Estimated Pi: 3.141567156
Julia Execution time:   2.423 s (0 allocations: 0 bytes)
-----------------------------------
```

_Note: the function is compiled first and then run again for the clocking._

![Horizontal bar plot with logaritmic x-axis showing a visual comparison of the 3 execution times.](comparison_barh_plot.png)

# Conclusions

As expected, `python` is by far the slower programming language. Surprisingly `Julia` is about 7.5 faster than the famous `C++`. Although both are in the same order of magnitude.

For another day: test whether this ratios are stable if the number of random points changes, or whether there are execution time optimised random value generator functions in specific packages.
