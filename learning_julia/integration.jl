using Plots
a = -1; b = 1; l=1000
x = range(a, b, length=l)
y = x.^2

gr()
plot(x, y, title="Quadratic Function", label="y = x^2")


# define a step function with 
# n = 10
# x_i = a + range/n * i
# h_i = x_i ^2

n = 10
i = 0:n
x_i = a .+ ((b-a)/n .* i)
h_i = x_i .^2

plot!(x_i, h_i, label="step function")
savefig("integration.png")
