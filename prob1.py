import numpy as np

# Open the input file for reading
with open("C:\\Users\\Varun\\OneDrive\\Desktop\\Workshop2024\\Milestone1\\Input\\Testcase4.txt", 'r') as f:
    lines = f.readlines()

# Create a dictionary to store key-value pairs from the input file
input_parameters = {}
for line in lines:
    key_value = line.split(":")
    input_parameters[key_value[0]] = int(key_value[1])

print(input_parameters)

# Calculate the radius based on WaferDiameter
wafer_radius = input_parameters['WaferDiameter'] // 2

# Function to generate points on a circle
def generate_points(num_points, angle, radius):
    theta = np.radians(angle)
    radii = np.linspace(-radius, radius, num_points)
    x_coordinates = radii * np.cos(theta)
    y_coordinates = radii * np.sin(theta)
    return x_coordinates, y_coordinates

# Generate points based on input parameters
circle_points = generate_points(input_parameters['NumberOfPoints'], input_parameters['Angle'], wafer_radius)
x_coordinates = list(circle_points[0])
y_coordinates = list(circle_points[1])

# Combine x and y coordinates into a list of tuples
list_of_points = [(x, y) for x, y in zip(x_coordinates, y_coordinates)]

# Print each point on a new line
for point in list_of_points:
    print(point)

# Write the points to an output file
with open('Output1.txt', 'w') as f:
    for point in list_of_points:
        f.write(f"({point[0]:.2f}, {point[1]:.2f})\n")
