using BenchmarkTools

function estimate_pi(n)
    inside_circle = 0
    for _ in 1:n
        x = rand()
        y = rand()
        if x^2 + y^2 <= 1.0
            inside_circle += 1
        end
    end
    return 4.0 * inside_circle / n
end

iterations = 1_000_000_000

println("Running Monte Carlo in Julia")


println("-----------------------------------")

# First run: Forces Julia to compile the function (and prints result)
result = estimate_pi(iterations)
println("Estimated Pi: ", result)

# Second run: Benchmarks the execute speed using Julia's native macro
print("Julia Execution time: ")
@btime estimate_pi($iterations)

print("-----------------------------------")
