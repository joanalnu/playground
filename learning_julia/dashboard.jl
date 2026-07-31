using Term
using Dates

# 1. Clear the terminal screen for a clean look
print("\e[2J\e[H")

# 2. Define styled text using Term's inline markup syntax {...}
header_text = """
{bold gold1}MANIFOLD OS -- THEORETICAL PHYSICS LAB{/bold gold1}
Current Time: $(Dates.format(now(), "HH:MM:SS")) | Active Mode: {bold light_blue}Study (Cosmology){/bold light_blue}
"""

# Create a top banner panel
banner = Panel(
    header_text,
    title = "System Header",
    style = "gold1 bold",
    justify = :center,
    box = :ROUNDED
)

# 3. Create Left Panel (System & Inventory Tracking)
left_content = """
{green}●{/green} Database Connection: {bold}Secure{/bold}
{green}●{/green} Background Daemon:   {bold}Active{/bold}

{underline gold1}Inventory Alerts:{/underline gold1}
{red}⚠ Coffee supply low (2 days left){/red}
{green}✓ Meal prep synced (High protein){/green}
"""

panel_left = Panel(
    left_content,
    title = "💡 System State",
    style = "light_blue",
    width = 40,
    box = :DOUBLE
)

# 4. Create Right Panel (Physics Math Computation Queue)
right_content = """
{yellow}⚙ Running Background Sim...{/yellow}
  ↳ [wCDM Grid Search]
  ↳ Progress: 74% Complete

{underline gold1}Next Academic Tasks:{/underline gold1}
  1. Derive Klein-Gordon energy-momentum tensor.
  2. Debug script.jl indexing error.
"""

panel_right = Panel(
    right_content,
    title = "🪐 Physics Core",
    style = "orange1",
    width = 44,
    box = :DOUBLE
)

# 5. Combine layouts using Term's intuitive math operators
# The '*' operator puts panels side-by-side
middle_row = panel_left * panel_right

# The '/' operator stacks layout blocks vertically
final_layout = banner / middle_row

# 6. Render the final TUI directly to your Kitty terminal
print(final_layout)
