import matplotlib.pyplot as plt


items = ["Python", "C++", "Julia"]
data = [140.1580, 10.056, 2.423] # for 1_000_000_000 points

fig, ax = plt.subplots()
ax.barh(items, data, align="center")
ax.yaxis.set_inverted(True)  # arrange data from top to bottom
ax.set_xlabel('Execution Time')
ax.set_xscale("log")
fig.savefig("comparison_barh_plot.png")
