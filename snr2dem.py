#Lowrance sonar csv-data converter

import pandas
import numpy as num


def xy2deg(x, y):
    rad2deg = 57.295779513082322
    earthRad = 6356752.3142

    lat = float(x / earthRad)
    lat = num.exp(lat)
    lat = (2 * num.arctan(lat)) - (num.pi / 2)
    lat = lat * rad2deg

    lon = float(y)
    lon = lon / earthRad * rad2deg

    return lat, lon

snrFile = 'Sonar0001.sl2.csv'
snrData = pandas.read_csv(snrFile)
posX = snrData.PositionX
posY = snrData.PositionY
if posX.size == posY.size:
    MAXVALUE = posX.size
else:
    print('Bad data file!')
    exit()

print(xy2deg(posX[0],posY[0]))