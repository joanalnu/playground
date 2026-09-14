import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Configuration and Data Generation
np.random.seed(42)
total_darts = 1000
fps = 20
frames = 100
darts_per_frame = total_darts // frames

x = np.random.uniform(0, 1, total_darts)
y = np.random.uniform(0, 1, total_darts)
inside_mask = (x**2 + y**2) <= 1.0

# Colors and styling
label_color = "#A0A0A0"
color_inside = "#00E5FF"   # Electric Cyan
color_outside = "#FF4081"  # Neon Pink
bg_color = "#111111"       # Dark background (GIFs handle transparency poorly, so a solid dark bg is best)

# 2. Figure Setup
fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

# Draw the unit circle quadrant boundary
theta = np.linspace(0, np.pi/2, 200)
ax.plot(np.cos(theta), np.sin(theta), color="#FFFFFF", linewidth=2, linestyle='--', label='Unit Circle Arc')

# Initialize empty scatter plots
scatter_inside = ax.scatter([], [], color=color_inside, s=20, alpha=0.8, label='Inside Circle')
scatter_outside = ax.scatter([], [], color=color_outside, s=20, alpha=0.8, label='Outside Circle')

# Formatting and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

title = ax.set_title(r"Estimating $\pi$: Throws = 0 | $\pi \approx 0.0000$", fontsize=14, pad=15, color=label_color)
ax.set_xlabel("$x$", fontsize=12, color=label_color)
ax.set_ylabel("$y$", fontsize=12, color=label_color)

# Style ticks, grid, and borders
ax.tick_params(axis='both', which='both', colors=label_color, labelsize=10)
ax.grid(True, linestyle='--', linewidth=0.5, color=label_color, alpha=0.3)

for spine in ax.spines.values():
    spine.set_color(label_color)

legend = ax.legend(frameon=True, facecolor='#222222', edgecolor='none', loc='lower right')
for text in legend.get_texts():
    text.set_color(label_color)

# 3. Animation Function
def animate(frame):
    # Determine how many darts to show in the current frame
    current_limit = (frame + 1) * darts_per_frame
    
    # Slice the arrays up to the current limit
    x_curr = x[:current_limit]
    y_curr = y[:current_limit]
    mask_curr = inside_mask[:current_limit]
    
    # Update scatter offsets (coordinates)
    inside_coords = np.column_stack((x_curr[mask_curr], y_curr[mask_curr]))
    outside_coords = np.column_stack((x_curr[~mask_curr], y_curr[~mask_curr]))
    
    scatter_inside.set_offsets(inside_coords if len(inside_coords) > 0 else np.empty((0, 2)))
    scatter_outside.set_offsets(outside_coords if len(outside_coords) > 0 else np.empty((0, 2)))
    
    # Calculate real-time Pi estimate
    inside_count = np.sum(mask_curr)
    pi_estimate = 4.0 * inside_count / current_limit
    
    # Update title
    title.set_text(f"Estimating $\\pi$: Throws = {current_limit} | $\\pi \\approx {pi_estimate:.4f}$")
    
    return scatter_inside, scatter_outside, title

# 4. Generate and Save Animation
print("Generating animation... this may take a moment.")
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000//fps, blit=True)

# Save as GIF
ani.save("darts_animation.gif", writer="pillow", fps=fps, savefig_kwargs={'facecolor': bg_color})
plt.close(fig)

print("GIF successfully generated as 'darts_animation.gif'!")
