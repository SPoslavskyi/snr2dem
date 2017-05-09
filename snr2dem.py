# Lowrance sonar csv-data converter
# Lowrance "Metric Mercator" to WGS84 LatLon deg

import pandas
import math
import numpy as num


def xy2deg(x, y):  # Convert XY to LatLon deg

    rad2deg = 57.295779513082321
    earthRad = 6356752.3142

    lat = float(y / earthRad)
    lat = num.exp(lat)
    lat = (2 * num.arctan(lat)) - (num.pi / 2)
    lat = lat * rad2deg

    lon = float(x)
    lon = lon / earthRad * rad2deg

    return lat, lon


def processData(x, y, d, d_valid, gridSize, dDif):
    lat = []
    lon = []
    depth = []
    lx = 0
    ly = 0
    ld = 0

    for i in range(0, MAX):
        if d_valid[i] == 'T':
            dist = math.sqrt((lx - x[i]) ** 2 + (ly - y[i]) ** 2)
            if dist == 0:
                continue
            cd = d[i] * 0.3048  # Converts ft to m
            dd = math.fabs(cd - ld) / dist
            if dist >= gridSize or dd >= dDif:
                tlat, tlon = xy2deg(x[i], y[i])
                lat.append(tlat)
                lon.append(tlon)
                depth.append(cd)
                lx = x[i]
                ly = y[i]
                ld = cd

    return lat, lon, depth


snrFile = 'Sonar0001.sl2.csv'
gridSize = 10
dDif = 0.5

snrData = pandas.read_csv(snrFile)
posX = snrData['PositionX']
posY = snrData['PositionY']
depth_ft = snrData['Depth[ft]']
depth_valid = snrData['DepthValid']

if posX.size == posY.size:
    MAX = posX.size
else:
    print('Bad data file!')
    exit()

lat, lon, depth = processData(posX, posY, depth_ft, depth_valid, gridSize, dDif)

print(lat, lon)
