import re
import math
import matplotlib.pyplot as plt
import seaborn as sns

# Configure Seaborn style & dark context aesthetics
sns.set_theme(style="darkgrid")
plt.style.use("dark_background")

# Configuration mapping file paths to log parsing rules
LOG_FILES = {
    "C++": "cpp/cpp_log.txt",
    "Julia": "julia/julia_log.txt",
    "Python": "python/python_log.txt"
}

# Values corresponding to evaluation inputs
POINTS = [1_000_000, 5_000_000, 1_000_000_000, 10_000_000_000]

def parse_log(filepath):
    """Extracts pi estimates and execution times (in seconds) from log files."""
    pi_estimates = []
    times = []
    
    with open(filepath, "r") as f:
        content = f.read()

    # Match Estimated Pi values
    pi_matches = re.findall(r"Estimated Pi:\s*([0-9.]+)", content)
    for p in pi_matches[:len(POINTS)]:
        pi_estimates.append(float(p))

    # Match execution times (handles 'seconds', 'ms', and 's')
    # Example matches: "(0.0115454 seconds)", "3.178 ms", "3.206 s", "0.2059 seconds"
    time_matches = re.findall(r"Execution time:\s*(?:[\w\s:]+?\()?([0-9.]+)\s*(ms|s|seconds)", content)
    
    for val, unit in time_matches[:len(POINTS)]:
        t = float(val)
        if unit == "ms":
            t /= 1000.0
        times.append(t)
        
    return pi_estimates, times

# Parse data from log files
data = {}
for lang, path in LOG_FILES.items():
    estimates, times = parse_log(path)
    data[lang] = {"estimates": estimates, "times": times}

# ---------------------------------------------------------
# Plot 1: Execution Time Comparison
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6))

label_color = "#808080"

for lang, val in data.items():
    ax.plot(
        POINTS, 
        val["times"], 
        label=lang, 
        marker='o', 
        linewidth=2, 
        markersize=5
    )

ax.set_xlabel("Total Points ($n$)", fontsize=12, color=label_color)
ax.set_ylabel("Execution Time (seconds)", fontsize=12, color=label_color)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_title("Monte Carlo $\pi$ Benchmark: Execution Time", fontsize=14, pad=12, color=label_color)

ax.tick_params(axis='both', which='both', colors=label_color, labelsize=10)
ax.grid(True, which='both', linestyle='--', linewidth=0.5, color=label_color, alpha=0.3)

# Style plot boundary lines (spines)
for spine in ax.spines.values():
    spine.set_color(label_color)

# Style legend text color
legend = ax.legend(frameon=True, facecolor='#222222', edgecolor='none')
for text in legend.get_texts():
    text.set_color(label_color)

# Export with transparent background
fig.savefig("report/comparison_barh_plot.png", dpi=600, transparent=True, bbox_inches='tight')
plt.close(fig)

# ---------------------------------------------------------
# Plot 2: Accuracy / Absolute Error Plot
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6))

# Plot reference line for true Pi
ax.axhline(0, color='red', linestyle='--', linewidth=1.5, label='True $\pi$ Error')

for lang, val in data.items():
    # Calculate absolute error |Estimate - Pi|
    errors = [abs(est - math.pi) for est in val["estimates"]]
    ax.plot(
        POINTS, 
        errors, 
        label=lang, 
        marker='o', 
        linewidth=2, 
        markersize=5
    )

ax.set_xlabel("Total Points ($n$)", fontsize=12, color=label_color)
ax.set_ylabel(r"Absolute Error $|\hat{\pi} - \pi|$", fontsize=12, color=label_color)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_title(r"Monte Carlo $\pi$ Estimate Convergence Error", fontsize=14, pad=12, color=label_color)

ax.tick_params(axis='both', which='both', colors=label_color, labelsize=10)
ax.grid(True, which='both', linestyle='--', linewidth=0.5, color=label_color, alpha=0.3)

# Style plot boundary lines (spines)
for spine in ax.spines.values():
    spine.set_color(label_color)

# Style legend text color
legend = ax.legend(frameon=True, facecolor='#222222', edgecolor='none')
for text in legend.get_texts():
    text.set_color(label_color)

# Export with transparent background
fig.savefig("report/accuracy.png", dpi=600, transparent=True, bbox_inches='tight')
plt.close(fig)

print("Plots generated successfully as transparent PNGs!")
