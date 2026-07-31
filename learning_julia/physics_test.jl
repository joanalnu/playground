using LinearAlgebra

println("--- Julia Physics Test ---")

# Define a 3x3 identity matrix and a random matrix
I3 = I(3) 
H = [1.0 0.0 2.0; 0.0 3.0 0.0; 2.0 0.0 1.0] # A symmetric Hamiltonian-like matrix

println("Matrix H:")
display(H)

println("\nEigenvalues of H:")
println(eigen(H).values)
