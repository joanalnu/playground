import numpy as np
import matplotlib.pyplot as plt

# Generate random points
np.random.seed(42)  # Fixed seed for reproducible plot
n_samples = 2_500
x = np.random.uniform(0, 1, n_samples)
y = np.random.uniform(0, 1, n_samples)

# Check inside vs outside unit circle
inside = (x**2 + y**2) <= 1.0

# Colors and styling
label_color = "#A0A0A0"
color_inside = "#00E5FF"   # Electric Cyan for inside circle
color_outside = "#FF4081"  # Neon Pink for outside circle

fig, ax = plt.subplots(figsize=(7, 7))

# Plot darts
ax.scatter(x[inside], y[inside], color=color_inside, s=12, alpha=0.7, label='Inside Circle ($r e \\leq 1$)')
ax.scatter(x[~inside], y[~inside], color=color_outside, s=12, alpha=0.7, label='Outside Circle ($r > 1$)')

# Draw the unit circle quadrant boundary
theta = np.linspace(0, np.pi/2, 200)
ax.plot(np.cos(theta), np.sin(theta), color="#FFFFFF", linewidth=2, linestyle='--', label='Unit Circle Arc')

# Formatting and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

ax.set_title(r"Monte Carlo Method: $\pi \approx 4 \times \frac{A_\text{circ}}{A_\text{square}}$", fontsize=14, pad=15, color=label_color)
ax.set_xlabel("$x$", fontsize=12, color=label_color)
ax.set_ylabel("$y$", fontsize=12, color=label_color)

# Style ticks, grid, and borders (spines)
ax.tick_params(axis='both', which='both', colors=label_color, labelsize=10)
ax.grid(True, linestyle='--', linewidth=0.5, color=label_color, alpha=0.3)

for spine in ax.spines.values():
    spine.set_color(label_color)

# Legend styling
legend = ax.legend(frameon=True, facecolor='#222222', edgecolor='none', loc='upper right')
for text in legend.get_texts():
    text.set_color(label_color)

# Export transparent image
fig.savefig("darts_simulation.png", dpi=600, transparent=True, bbox_inches='tight')
plt.close(fig)

print("Dart simulation plot successfully generated as 'darts_simulation.png'!")
