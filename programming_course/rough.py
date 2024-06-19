import matplotlib.pyplot as plt

# Define the points
x = [0, 3, 9, 4, 7]
y = [2, 8, 18, 10, 16]

# Create the line plot
plt.line(x,y, '.')  # 'marker' adds markers at the data points

# Optionally, add titles and labels
plt.title('Line Plot of Given Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()
