import matplotlib.pyplot as plt

x0 = 0
y0 = 0
x = 0
y = 0

ax = plt.axes()
ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])
ax.quiver(x0, y0, x, y, angles="xy", scale_units="xy", scale=1, color="red")
ax.grid()

plt.plot([-4, 4], [0, 0], color="gray")
plt.plot([0, 0], [-4, 4], color="gray")
plt.show()