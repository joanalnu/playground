import matplotlib.pyplot as plt
plt.style.use("dark_background")

items = ["C++", "Julia", "Python"]
points = [1000000, 5000000, 1000000000]
cpp_data = [0.0115454, 0.0552192, 10.8913] # seconds
julia_data = [0.003178, 0.015893, 3.206] # secondsds
python_data = [0.2059, 0.9752, 195.5452] # seconds


fig, ax = plt.subplots(figsize=(8,6))
ax.plot(points, cpp_data, label=items[0], marker='x', markersize=6)
ax.plot(points, julia_data, label=items[1], marker='x', markersize=6)
ax.plot(points, python_data, label=items[2], marker='x', markersize=6)
ax.set_xlabel('Total points (n)')
ax.set_ylabel('Execution time')
ax.set_xscale('log')
ax.set_yscale('log')
plt.legend()
plt.title("Execution Time Comparison Plot")
fig.savefig("comparison_barh_plot.png", dpi=600)

plt.close()
# create plot of the accuracy of the results
import math

cpp_est = [3.13931, 3.14114, 3.14166]
julia_est = [3.13936, 3.1417928, 3.141578452]
python_est = [3.143456, 3.1411936, 3.141586808]

fig, ax = plt.subplots(figsize=(8,6))
ax.hlines(math.pi, min(points), max(points), colors='r', linestyles='--')
ax.plot(points, cpp_est, label=items[0], markersize=8)
ax.plot(points, julia_est, label=items[1], markersize=8)
ax.plot(points, python_est, label=items[2], markersize=8)
ax.set_xlabel('Total points (n)')
ax.set_ylabel(r'$\Delta \pi$')
ax.set_xscale('log')
plt.legend()
plt.title(r'$\pi$ Estimate Accuracy')
fig.savefig('accuracy.png', dpi=600)
