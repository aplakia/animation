import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# Create a default figure and subplot
fig, ax = plt.subplots()
# Specify x - y axes' range respectively
ax.axis([0,6,0,6])
# set background colour
ax.set_axis_bgcolor('grey')
# Draw a two-dimensional point of circle shape with specific characteristics
circle_point, = ax.plot(3, 3, 'o', markerfacecolor='w', markeredgecolor='red', markersize=3,
 markeredgewidth = 3)
# Draw first frame
def init():
 return circle_point,
 # Draw frame
def animate(i):
  if i < 100:
      j = 0
  else:
      j = i - 97
  if i < 200:
      k = 0
  else:
      k = i - 197
  # Update circle point's position
  circle_point,=ax.plot(3, 3, 'o', markerfacecolor='red', markeredgecolor = 'red', markersize = i, markeredgewidth = 3 )
  circle_point1,=ax.plot(3, 3, 'o', markerfacecolor='orange', markeredgecolor = 'orange', markersize = j, markeredgewidth = 3 )
  return [circle_point, circle_point1,]
   # Interval draws a new frame every given milliseconds
ani = animation.FuncAnimation(fig, animate, np.arange(3, 300),
init_func=init, interval=25)
ani.save("wave.mp4", fps=40)