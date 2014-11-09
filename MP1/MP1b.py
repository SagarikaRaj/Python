
from __future__ import print_function #to override the existing print function and enable it to add separators
import random

# Creating a random list of 3-tuples 
threeSpace = [(random.randint(-1000,1000),random.randint(-1000,1000),random.randint(-1000,1000))] #list initialization
counter = 1
while (counter <= 100) :
    threeSpace.insert(counter,(random.randint(-1000,1000),random.randint(-1000,1000),random.randint(-1000,1000))) 
    counter  = counter + 1

#Sorting along each of the axes
zSortedSpace = sorted(threeSpace, key=lambda coord:coord[2])
ySortedSpace = sorted(threeSpace, key=lambda coord:coord[1])
xSortedSpace = sorted(threeSpace, key=lambda coord:coord[0])

#print the sorted spaces in the required format
print ("X-SORTING    ","Y-SORTING    ","Z-SORTING", sep = '\t\t')
print ("----------------------------------------------------------------",sep='')
i = 0
while(i<100):
    print (xSortedSpace[i],ySortedSpace[i],zSortedSpace[i],sep ='\t')
    i+=1


#finding the distance of each point and adding it to the dictionary along with its tuple values
import math
distanceDictionary = {threeSpace[0]:math.sqrt((abs(threeSpace[0][0])**2)+(abs(threeSpace[0][1])**2)+(abs(threeSpace[0][2])**2))}
i = 1
j = 1
while (i<100):
    distanceDictionary[threeSpace[i]] = abs(threeSpace[i][0])**2
    j = 1
    while(j<3):
        distanceDictionary[threeSpace[i]] = distanceDictionary.get(threeSpace[i])+ abs(threeSpace[i][j])**2
        j = j+1
        
    distanceDictionary[threeSpace[i]] = math.sqrt(distanceDictionary.get(threeSpace[i]))
    i = i + 1

print ("\n\nPRINTING UNSORTED DICTIONARY",sep='')
print (distanceDictionary,sep='')

#Sorting the dictionary 
print ("\n\nPRINTING SORTED DICTIONARY",sep='')
sortedDictionary = [x for x in distanceDictionary.iteritems()] 
sortedDictionary.sort(key=lambda x: x[1])
print (sortedDictionary,sep='')

#Assigning minCoord and maxCoord
import copy
minCoord  = {}
minCoord = copy.copy(sortedDictionary[0][0])
maxCoord  = {}
maxCoord = copy.copy(sortedDictionary[99][0])

print ("\n \n CO ORDINATE WITH MINIMUM DISTANCE TO ORIGIN",sep='')
print (minCoord,sep='')
print ("CO ORDINATE WITH MAXIMUM DISTANCE TO ORIGIN",sep='')
print (maxCoord,sep='')