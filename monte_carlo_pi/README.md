# Scope

Using both `python` and `julia` to estimate $\pi$ using monte carlo simulation (typical throwing darts to a cricle in a square example), to demonstrate the compiling time of each language and the power of `julia`.

# Files

- `est_pi.py`: estimating $\pi$ using `python`, uses the `time` package for time keeping.
- `j_est_pi.py`: estimating $\pi$ using `julia`, uses the `BenchmarkTools` package to keep time.

# Dependencies

You need to have installed both languages to run the code.

Install the `BenchmarkTools` for julia using 
```zsh
julia -e 'using Pkg; Pkg.add("BenchmarkTools")'
```

# Results

### Python

With system wide `python` (Python 3.14.6):
```
Result: 3.141976
Python execution time: 2.7619 seconds
```

with `venv` `python` (Python 3.14.6):
```
Result: 3.1421618
Python execution time: 2.7776 seconds
```

### Julia

With `julia` (julia version 1.12.6):
```
Result: 3.141708
Julia Execution time:   48.127 ms (0 allocations: 0 bytes)
```

# Conclusions

There is barely no difference between the system wide and the virtual environemnt (`venv`) python execution time. `venv`s really are only useful for compartimentalisation and package version handling, indeed the `venv` `python` took more than 10 ms longer to run.

In comparison with `julia`'s execution time (48.127 ms), it executes the same code in about 57 times faster.
