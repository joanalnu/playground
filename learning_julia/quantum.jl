using DifferentialEquations
using LinearAlgebra
using UnicodePlots

println("Initializing Quantum Wave Packet Simulation...")

# 1. Setup the Spatial Grid (The 1D Box)
const N = 100            # Number of spatial grid points
const dx = 0.1           # Spatial step size
const x = range(-5.0, 5.0, length=N)

# 2. Define the Initial Wave Function ψ(x, t=0)
# A Gaussian wave packet moving to the right with momentum k₀
const k0 = 10.0
const σ = 0.5
ψ0 = ComplexF64[exp(- (xi)^2 / (2*σ^2)) * exp(im * k0 * xi) for xi in x]
# Normalize the wave function so total probability equals 1
ψ0 ./= norm(ψ0) * sqrt(dx)

# 3. Construct the Hamiltonian Matrix (H = T + V)
# Kinetic energy operator (T) using standard finite difference for the 2nd derivative
T = zeros(ComplexF64, N, N)
for i in 1:N
    T[i, i] = -2.0
    if i > 1;  T[i, i-1] = 1.0; end
    if i < N;  T[i, i+1] = 1.0; end
end
T .*= -0.5 / dx^2  # Assuming h-bar = m = 1 for simplicity

# Potential energy operator (V) - Let's place a potential barrier on the right side
V = zeros(Float64, N)
for i in 1:N
    if x[i] > 1.5 && x[i] < 2.0
        V[i] = 40.0  # The barrier height
    end
end
H = T + Diagonal(V)

# 4. Define the Schrödinger Equation: dψ/dt = -i * H * ψ
# Because we are using an imaginary 'im', we use -im * H * ψ
schrodinger!(dψ, ψ, p, t) = mul!(dψ, -im * H, ψ)

# 5. Solve the Differential Equation over time
tspan = (0.0, 0.4)
prob = ODEProblem(schrodinger!, ψ0, tspan)
sol = solve(prob, Tsit5(), reltol=1e-6, abstol=1e-6)

# 6. Visualize the Probability Density |ψ|² at different times in Kitty!
println("\n--- Quantum Simulation Results ---")
for t_val in [0.0, 0.15, 0.35]
    ψ_t = sol(t_val)
    prob_density = abs2.(ψ_t)
    
    # Generate a beautiful terminal line plot
    plt = lineplot(x, prob_density, 
                   title="Probability Density |ψ|² at t = $t_val", 
                   xlabel="Position (x)", ylabel="Probability", 
                   width=60, height=10)
    display(plt)
    println("\n" * "="^70 * "\n")
end
