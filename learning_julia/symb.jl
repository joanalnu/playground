using Symbolics

@variables t H0
Dt = Differential(t)

a = exp(H0 * t)
da_dt = expand_derivatives(Dt(a))

println("t = ", t)
println("H0 = ", H0)
println("a = ", a)
println("da_dt = ", da_dt)
