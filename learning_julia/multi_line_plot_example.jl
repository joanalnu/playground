using UnicodePlots

x = range(0, 2π, length=40)
y1 = sin.(x)
y2 = cos.(x)
y3 = tan.(x)

# 1. Create the base plot with sin(x)
my_plot = lineplot(x, y1, title="Trig Functions", name="sin(x)")

# 2. Add cos(x) onto the same canvas
lineplot!(my_plot, x, y2, name="cos(x)")
lineplot!(my_plot, x, y3, name="tan(x)")

# 3. Render it in Kitty
display(my_plot)



# -----------------------------------------------------
# Creating an actual image
using Plots

# 1. Create the base plot
# GR is the default high-speed backend for generating images
gr()

plot(x, y1, title="Trig Functions", label="sin(x)", linewidth=2)

# 2. add the other lines using plot!
plot!(x, y2, label="cos(x)", linewidth=2)
plot!(x, y3, label="tan(x)", linewidth=2)

# 3. save the result
Plots.savefig("trig_functions.png")
