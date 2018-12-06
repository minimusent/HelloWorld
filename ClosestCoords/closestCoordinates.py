import math

# Coordinates either read in as list or through existing external file
coordinates = [
    [1,   0.0,    0.0],
    [2,  10.1,  -10.1],
    [3, -12.2,   12.2],
    [4,  38.3,   38.3],
    [5, 79.99, 179.99]
    ]

class Point:
    def __init__(self, ID, x, y):
        self.ID = ID
        self.x = x
        self.y = y
        self.distanceList = []
        self.closest = []

newCoords = []

for coordinate in coordinates:
    newCoords.append(Point(coordinate[0], coordinate[1], coordinate[2]))

def get_distance(c1,c2):
    return math.sqrt( ((c2[0] - c1[0])**2)+((c2[1]-c1[1])**2) )

for coordinate in newCoords:
    p1 = coordinate
    for coordinate in newCoords:
        p2 = coordinate
        distance = round(get_distance([p1.x,p1.y],[p2.x,p2.y]),2)
        if distance > 0:
            p1.distanceList.append([distance,p2.ID])
            p1.distanceList.sort()
            p1.closest.append(p2.ID)
    p1.closest = p1.closest[:3]


for coordinate in newCoords:
    print(str(coordinate.ID) + ', '+str(coordinate.closest))
