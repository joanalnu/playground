import matplotlib.pyplot as plt

items = ["C++", "Julia", "Python"]
points = [1000000, 5000000, 1000000000]
cpp_data = [0.0115454, 0.0552192, 10.8913] # seconds
julia_data = [0.003178, 0.015893, 3.206] # secondsds
python_data = [0.2059, 0.9752, 195.5452] # seconds


fig, ax = plt.subplots(figsize=(8,6))
ax.plot(points, cpp_data, label=items[0])
ax.plot(points, julia_data, label=items[1])
ax.plot(points, python_data, label=items[2])
ax.set_xlabel('Total points (n)')
ax.set_ylabel('Execution time')
ax.set_xscale('log')
ax.set_yscale('log')
plt.legend()
plt.title("Execution Time Comparison Plot")
fig.savefig("comparison_barh_plot.png", dpi=600)
