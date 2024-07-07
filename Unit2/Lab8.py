from collections import namedtuple

Point = namedtuple('P', ['x','y'])

p1 = Point(3,5)
p2 = Point(-1,2)

print("Coordinates of p1:",p1.x,p2.y)
