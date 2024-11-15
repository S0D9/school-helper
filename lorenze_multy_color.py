import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Parameters for the Lorenz system
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Time step and number of steps
dt = 0.01
num_steps = 10000

# Arrays to hold the values of x, y, z
x = np.empty(num_steps + 1)
y = np.empty(num_steps + 1)
z = np.empty(num_steps + 1)

# Initial values
x[0], y[0], z[0] = 0.0, 1.0, 1.05

# Function to calculate the Lorenz equations
def lorenz(x, y, z, sigma, rho, beta):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

# Calculate points for the Lorenz attractor
for i in range(num_steps):
    dx, dy, dz = lorenz(x[i], y[i], z[i], sigma, rho, beta)
    x[i + 1] = x[i] + dx * dt
    y[i + 1] = y[i] + dy * dt
    z[i + 1] = z[i] + dz * dt

# Create color values based on the position in the trajectory
colors = np.linspace(0, 1, num_steps)

# Plot the Lorenz attractor with color gradient
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Create a colormap
norm = Normalize()
colormap = plt.cm.plasma

for i in range(num_steps - 1):
    ax.plot(x[i:i+2], y[i:i+2], z[i:i+2], color=colormap(norm(colors[i])), lw=0.5)

ax.set_title("Lorenz Attractor (Multicolor)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Add a color bar to indicate the progression of time
sm = ScalarMappable(cmap=colormap, norm=norm)
sm.set_array([])
plt.colorbar(sm, ax=ax, fraction=0.02, pad=0.1, label="Time progression")

plt.show()
