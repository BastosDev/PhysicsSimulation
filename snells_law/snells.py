import numpy as np
import matplotlib.pyplot as plt

n1 = 1.00 # air
n2 = 1.33 # water
# Refractive indices commonly used for air and water
theta1_deg = 46
theta1_rad = np.radians(theta1_deg) 
# angle of incidence
# numpy only works with radians
arg = (n1/n2) * np.sin(theta1_rad)
# Calculating the arg for the arcsin
if arg > 1:
    print("No refraction.")
else:
    theta2_rad = np.arcsin(arg)
    # Calculating the angle of refraction using Snell's law
    theta2_deg = np.degrees(theta2_rad)
    # Converting the angle of refraction back to degrees for easier interpretation
    print(f"Angle of refraction: {theta2_deg:.2f} degrees")
x_inc = [-np.tan(theta1_rad), 0]
y_inc = [1, 0]
# Coordinate for the incident ray
x_ref = [0, np.tan(theta2_rad)]
y_ref = [0, -1]



# --- Ploting ---
plt.figure(figsize=(8, 6))

plt.axhline(0, color='black', lw=2, label='Interface (Fronteira)')

plt.axvline(0, color='gray', linestyle="--", label='Interface')

plt.plot(x_inc, y_inc, label='Incident Ray (Raio Incidente)', color='red')

plt.plot(x_ref, y_ref, label='Refracted Ray (Raio Refratado)', color='blue')

plt.title(f"Snell's Law Simulation: n1={n1} (Air) , n2={n2} (Water)")
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()