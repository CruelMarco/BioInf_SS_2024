import pulp

# Create a binary integer programming problem
prob = pulp.LpProblem("Sandbox_Cover", pulp.LpMinimize)

# Define decision variables
x = pulp.LpVariable.dicts("x", range(1, 12), cat='Binary')  # Whether to use a 200cm panel in each row
y = pulp.LpVariable.dicts("y", [(i, j) for i in range(1, 12) for j in range(1, 3)], cat='Binary')  # Whether to cut each panel

# Objective function
prob += pulp.lpSum(x)

# Constraints
for i in range(1, 12):
    # Each row must be covered
    prob += 100*(1-y[(i, 1)]) + 200*y[(i, 1)] + 100*(1-y[(i, 2)]) + 200*y[(i, 2)] >= 105*x[i]

    # No panel should be shorter than 20cm
    prob += 100*(1-y[(i, 1)]) + 200*y[(i, 1)] >= 20
    prob += 100*(1-y[(i, 2)]) + 200*y[(i, 2)] >= 20

    if i < 11:
        # If two panels are joined, the seam must be at least 10cm apart
        prob += 100*(1-y[(i, 1)]) + 100*(1-y[(i+1, 1)]) + 200*y[(i, 1)] + 200*y[(i+1, 1)] >= 110

# Solve the ILP
prob.solve()

# Print the optimal objective value
print("Optimal Objective Value (Minimum number of 200cm panels needed):", pulp.value(prob.objective))

# Print the optimal solution
print("\nOptimal Solution:")
for i in range(1, 12):
    if pulp.value(x[i]) == 1:
        print("Row", i, ": 200cm panel")
    else:
        print("Row", i, ": 100cm panels")
