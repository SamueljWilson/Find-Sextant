import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

class XY_plane:
    def __init__(self, coordinate):
        self.coord = coordinate
        self.x = float(self.coord[0])
        self.y = float(self.coord[1])


def findConnectingLine(coord1, coord2):
    def lineFunc(x):
        return (coord1.y - coord2.y)/(coord1.x - coord2.x)*(x - coord1.x) + coord1.y
    return lineFunc

# The sextants increase counterclockwise starting at the leftmost sextant
def find_sextant(robot_pos, line_1, line_2, line_3):
    is_robot_under_line = lambda robot_pos, line: True if robot_pos.y < line(robot_pos.x) else False
    under_L1 = is_robot_under_line(robot_pos, line_1)
    under_L2 = is_robot_under_line(robot_pos, line_2)
    under_L3 = is_robot_under_line(robot_pos, line_3)
    if under_L1:
        if under_L3:
            if under_L2:
                return("3")
            else:
                return("4")
        else:
            return("5")
    elif under_L2:
        if under_L3:
            return("2")
        else:
            return("1")
    else:
        return("6")

# Coordinates of the vertexes of the hexagon (Starting bottommost and increasing counterclockwise)
V1 = XY_plane((4.475346,3.158854))
V2 = XY_plane((5.351533,3.618320))
V3 = XY_plane((5.330640,4.570682))
V4 = XY_plane((4.513791,5.057343))
V5 = XY_plane((3.704928,4.570636))
V6 = XY_plane((3.696494,3.636104))

# Returns the function of the line that connects both vertices together
line_1 = findConnectingLine(V1, V4)
line_2 = findConnectingLine(V2, V5)
line_3 = findConnectingLine(V3, V6)

robot_pos = XY_plane((6, 8))

print(find_sextant(robot_pos, line_1, line_2, line_3))

# Only used for helping to visualise the field
fig, ax = plt.subplots()
hexagon = Polygon([V1.coord, V2.coord, V3.coord, V4.coord, V5.coord, V6.coord], edgecolor='red', facecolor="grey")
ax.add_patch(hexagon)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
x_1 = np.linspace(0, 10)
y_1 = line_1(x_1)
x_2 = np.linspace(0, 10)
y_2 = line_2(x_1)
x_3 = np.linspace(0, 10)
y_3 = line_3(x_1)
plt.plot(x_1, y_1 , 'green')
plt.plot(x_2, y_2, 'blue')
plt.plot(x_3, y_3, 'purple')
plt.plot(robot_pos.x, robot_pos.y, 'ro')
plt.show()
