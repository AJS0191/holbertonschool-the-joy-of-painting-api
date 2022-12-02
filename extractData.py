#!/usr/bin/env python3
"""this script is used to extract data
from the painting/date data and store 
the important data in a dictionary and export
or save in a new file"""

allData = open('c:/Developing/holbertonschool-the-joy-of-painting-api/paintingDates')
dataList = list(allData)
splitData = []

"""split each line by '(' resulting in 2 piece array name 
at index 0 and data at index 1"""

for line in dataList:
    pieces = line.split('(')
    splitData.append(pieces)

"""print(splitData)"""
"""remove the ')/n' from the dates and extra "and\ from name"""
for couple in splitData:
    couple[0] = couple[0].replace('" ', '').replace('"', '')
    couple[1] = couple[1].split(')')[0]

"""splitData now holds all useable data in splitData at indexes 0 and 1"""

"""build dictionary that will be basis for painting obj and table"""

paintings = {}
i = 0
for couple in splitData:
    paintings[i] = {'name': couple[0], 'date': couple[1], 'month': couple[1].split(' ')[0]}
    i = i + 1

allData.close()

"""this part of the script is used to extract data
from the painting/colors data and store 
the important data into dictionaries and export
or save in a new file"""

allData = open('c:/Developing/holbertonschool-the-joy-of-painting-api/paintingColors')
dataList = list(allData)
splitData = []
colorData = []
hexData = []

"""from line 0 extract list of all color names"""
line0 = dataList[0].split('color_hex,')[1]
colorList = line0.replace('_', ' ').replace('\n', '').split(',')

"""all colors are in colorList"""
"""from each line in dataList extract img link, name, vid link, list of colors
to dictionary for comparison and combination with paintings dictionary
extract color list and list of hexes to build a colordictionary

index 3 is name
index 2 is img link
index 7 is youtube link
"""

i = 1
while i < len(dataList):
    line = dataList[i]
    couple = line.split('[')
    pieces = couple[0].split(',')
    splitData.append(pieces)
    colorData.append(couple[1])
    hexData.append(couple[2])
    i = i+1

colorLines = []
"""clean up color data"""
for line in colorData:
    split = line.split(']')
    colorLines.append(split[0].replace('\\r\\n', ''))
colorData = []

for line in colorLines:
    split = line.replace("'", '').split(', ')
    colorData.append(split)

"""colorData is still indexed same as dataList and can be appended to paintings dictionary
now to clean up the hexes"""

colorLines = []
for line in hexData:
    colorLines.append(line.split(']')[0])

hexData = []
for line in colorLines:
    hexData.append(line.replace("'", '').split(', '))

""" combine hexdata and color data to make color dictionary """
i = 0
j = 0

while
