#Lowrance sonar csv-data converter

import pandas

snrFile = 'Sonar0001.sl2.csv'
snrData = pandas.read_csv(snrFile)

