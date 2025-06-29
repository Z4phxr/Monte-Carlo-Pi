import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import random


def cords_generator(r):
    """
    Infinite generator that yields random (x, y) points within a square [-1, 1] x [-1, 1]
    and a boolean indicating whether the point lies inside the circle with radius r.

    Args:
        r (float): Radius of the circle.

    Yields:
        tuple: (x, y, is_in_circle) where is_in_circle is True if (x, y) is inside the circle.
    """
    while True:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        yield x, y, x * x + y * y <= r * r


# Set up the figure and axes
fig, ax = plt.subplots()

# Add a unit circle to represent the boundary
circle = patches.Circle((0, 0), 1, edgecolor='black', facecolor='none', linewidth=1)
ax.add_patch(circle)

# Set equal aspect ratio and limits for x and y axes
ax.set_aspect('equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
fig.canvas.manager.set_window_title('Monte Carlo Pi Approximation')

# Initialize point generator with radius 1
cords = cords_generator(1)

# Lists to store inside and outside points
in_points = []
out_points = []

# Initialize empty plots for points
in_plot, = ax.plot([], [], 'go', markersize=3)   # green points (inside circle)
out_plot, = ax.plot([], [], 'ro', markersize=3)  # red points (outside circle)


def update(i):
    """
    Update function for animation. Adds 10 random points each frame,
    updates the plot, and computes the approximation of Pi.

    Args:
        i (int): Frame index (not used but required by FuncAnimation).

    Returns:
        tuple: Updated plots for inside and outside points.
    """
    for _ in range(10):  # Add 10 points per frame
        x, y, is_in_circle = next(cords)
        if is_in_circle:
            in_points.append((x, y))
        else:
            out_points.append((x, y))

    # Update data for plots
    in_plot.set_data(*zip(*in_points) if in_points else ([], []))
    out_plot.set_data(*zip(*out_points) if out_points else ([], []))

    # Calculate and display approximation of Pi
    pi_approximation = 4 * len(in_points) / (len(in_points) + len(out_points))
    ax.set_title(f'PI ≈ {pi_approximation:.6f}', fontsize=16)

    return in_plot, out_plot


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=300, interval=1, blit=False)

# Display the plot
plt.show()
