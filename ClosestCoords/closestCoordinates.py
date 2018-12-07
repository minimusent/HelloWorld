import math

# Coordinates either read in as list or through existing external file
coordinates = [
    [1,   0.0,    0.0],
    [2,  10.1,  -10.1],
    [3, -12.2,   12.2],
    [4,  38.3,   38.3],
    [5, 79.99, 179.99],
    ]

class Point:
    def __init__(self, ID, x, y):
        self.ID = ID
        self.x = x
        self.y = y
        self.distanceList = []
        self.closest = []

newCoords = []

# Convert coordinate list into Point classes
for coordinate in coordinates:
    newCoords.append(Point(coordinate[0], coordinate[1], coordinate[2]))

# Return distance
def get_distance(c1,c2):
    return math.sqrt( ((c2[0] - c1[0])**2)+((c2[1]-c1[1])**2) )

# Get distance for each coordinate, sort by distance, add closest coordinates to list
for coordinate in newCoords:
	p1 = coordinate
	for coordinate in newCoords:
		if not coordinate == p1:
			p2 = coordinate
			distance = get_distance([p1.x,p1.y],[p2.x,p2.y])
			p1.distanceList.append([distance,p2.ID])
	p1.distanceList.sort()
	for distance, ID in p1.distanceList:
		p1.closest.append(ID)
	p1.closest = p1.closest[:3]

# Display results
for coordinate in newCoords:
    print(str(coordinate.ID)+ ' ' + str(','.join(str(closest) for closest in coordinate.closest)))
