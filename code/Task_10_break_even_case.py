import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Case: break-even point for a small mandazi shop
price = 60.0          # selling price per mandazi (KES)
fixed_cost = 5000.0   # rent and equipment (KES)
unit_cost = 20.0      # cost to make one mandazi (KES)
extra_cost = 0.01     # extra cost that grows with volume

def profit(q):
    income = price * q
    cost = fixed_cost + unit_cost * q + extra_cost * q**2
    return income - cost

# Bisection: profit is negative at 0 sales and positive at 1000 sales
solution = root_scalar(
    profit,
    bracket=[0, 1000],
    method="bisect",
    xtol=1e-10
)

break_even = solution.root

print(f"Profit at 0 sales: {profit(0):.2f} KES")
print(f"Profit at 1000 sales: {profit(1000):.2f} KES")
print(f"Break-even quantity: {break_even:.2f} mandazi")
print(f"Income at break-even: {price * break_even:.2f} KES")
print(f"Bisection iterations: {solution.iterations}")

quantities = np.linspace(0, 1000, 300)
plt.plot(quantities, profit(quantities))
plt.axhline(0, linewidth=0.8)
plt.axvline(break_even, linestyle="--")
plt.xlabel("Number of mandazi sold")
plt.ylabel("Profit (KES)")
plt.title("Break-even point of a small shop")
plt.grid(True)
plt.savefig("docs/Task_10_break_even_graph.png")
plt.show()