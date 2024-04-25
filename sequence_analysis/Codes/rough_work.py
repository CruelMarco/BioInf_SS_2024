import numpy as np
import matplotlib.pyplot as plt

# Define the inequalities
def inequality1(x1, x2):
    return -x1 + 2*x2 <= 3

def inequality2(x1, x2):
    return 3*x1 + 4*x2 <= 22

def inequality3(x1, x2):
    return -x1 - 3*x2 <= -3

def x1_nonnegativity(x1):
    return x1 >= 0

def x2_nonnegativity(x2):
    return x2 >= 0

# Create a grid of points
x1_vals = np.linspace(0, 10, 400)
x2_vals = np.linspace(0, 10, 400)
X1, X2 = np.meshgrid(x1_vals, x2_vals)

# Evaluate the inequalities on the grid
ineq1 = inequality1(X1, X2)
ineq2 = inequality2(X1, X2)
ineq3 = inequality3(X1, X2)
ineq4 = x1_nonnegativity(X1)
ineq5 = x2_nonnegativity(X2)

# Combine all inequalities
feasible_region = ineq1 & ineq2 & ineq3 & ineq4 & ineq5

# Plotting the feasible region
plt.figure(figsize=(8, 8))
plt.title('Feasible Region')

# Shade the feasible region
plt.fill_between(x1_vals, 0, 10, where=(feasible_region), color='gray', alpha=0.5)

# Plot the inequalities
plt.plot(x1_vals, (3 + x1_vals)/2, label='-x1 + 2x2 <= 3', color='blue')
plt.plot(x1_vals, (22 - 3*x1_vals)/4, label='3x1 + 4x2 <= 22', color='green')
plt.plot(x1_vals, (-3 + x1_vals)/(-3), label='-x1 - 3x2 <= -3', color='red')

# Highlight axes
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Set limits and labels
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('x1')
plt.ylabel('x2')

# Display legend
plt.legend()

# Show plot
plt.grid(True)
plt.show()
