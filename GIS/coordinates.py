
#Takes csv filename as argument and returns a list of coordinates.
def getCoordinates(file):
    import csv

    coordFile = open(file, "r")

    csvReader = csv.reader(coordFile)

    header = next(csvReader)

    latIndex = header.index("lat")
    lonIndex = header.index("long")

    coords = []

    #Add each lat/lon as a set of coordinates to the list
    for row in csvReader:
        lat = row[latIndex]
        lon = row[lonIndex]
        coords.append([lat,lon])

    coordFile.close()

    return coords

coords = getCoordinates("coords.csv")

for lat, lon in coords:
    print(lat + ", "+ lon)
