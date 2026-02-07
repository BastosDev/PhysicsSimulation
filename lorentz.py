import numpy as np
import matplotlib.pyplot as plt

delta_time = 0.01
# Delta time is the time step for the calculation. A smaller delta time will give a more accurate result, but will take longer to compute.
steps = 1000
# Steps basicaly is the number of interations(1 per delta time).
print("Tools are ready")
# Propreits of particles
q = 1 # Charge of the particle
m = 1 # Mass of the particle
hist_x = []
hist_y = []
hist_z = []
# Where the particle will be at each time step
initial_position = np.array([0.0, 0.0, 0.0])
# Initial position of the particle
velocity = np.array([1.0, 0.0, 1.0])
# Initial velocity of the particle
# The velocity is pointing in the x and z direction(moving in the xz plane)
B = np.array([0.0, 0.0, 5.0])

print ("Vectors are ready")
print (f"Initial velocity: {velocity}")
print (f"Magnetic field: {B}")

initial_F = q * np.cross(velocity, B)
# The Lorentz force is the ponds of the charge, the velocity and the magnetic field(F = q * v x B)
print (f"Initial Lorentz force: {initial_F}")
print ("Starting simulation...")

for i in range(steps):
    F = q * np.cross(velocity, B)
    # Calculating the Lorentz force at each time step
    acc = F / m
    # Calculating the acceleration using Newton's second law (F = m * a)
    velocity += acc * delta_time
    # Updating the velocity using the acc and the delta time (v = v + a * dt)
    initial_position += velocity * delta_time
    # Updating the postion using the velocity and the delta time (x = x + v * dt)
    hist_x.append(initial_position[0])
    hist_y.append(initial_position[1])
    hist_z.append(initial_position[2])
    # Saving the position at each time for the graph
print ("Simulation finished, data collected")

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
# Creating a 3D plot
ax.plot(hist_x, hist_y, hist_z, label="Electron", color="blue")
# Making the trajectory of the particle
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title(f"Lorentz Force Simulation (v={velocity}, B={B})")
# Setting the labels and title of the graph
ax.legend()
# Adding a legend to the graph
plt.show()
# Displaying the graph