#getting data from the given url
from urllib import urlopen
url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()

#initializing 26 lists each holding a counter for words starting with the corresponding letter
threeSpace = ['a',0,0] #alphabet with which the word starts, number of occurrences, percentage of occurrence
listb = ['b',0,0]
listc = ['c',0,0]
listd = ['d',0,0]
liste = ['e',0,0]
listf = ['f',0,0]
listg = ['g',0,0]
listh = ['h',0,0]
listi = ['i',0,0]
listj = ['j',0,0]
listk = ['k',0,0]
listl = ['l',0,0]
listm = ['m',0,0]
listn = ['n',0,0]
listo = ['o',0,0]
listp = ['p',0,0]
listq = ['q',0,0]
listr = ['r',0,0]
lists = ['s',0,0]
listt = ['t',0,0]
listu = ['u',0,0]
listv = ['v',0,0]
listw = ['w',0,0]
listx = ['x',0,0]
listy = ['y',0,0]
listz = ['z',0,0]

#creating a dictionary with key, value = word, counter for occurrences
origDictionary = {'the':0}

#counter for keeping track of the total number of words
totalWordsCounter = 0
para = raw.split()

for word in para:
    if(word.isalpha()):
        totalWordsCounter = totalWordsCounter+1 #counter for total number of words
        lowerCaseWord = word.lower() #converting all words into lowercase
                   
        #adding to the counter if the word already exists/adding a new entry into dictionary if the word does not exist
        if (origDictionary.has_key(lowerCaseWord)):
            origDictionary[lowerCaseWord] = origDictionary[lowerCaseWord]+1
        else:
            origDictionary[lowerCaseWord] = 1
            
        #adding the word to a corresponding list
        if(lowerCaseWord.startswith('a',0)):
            threeSpace[1] = threeSpace[1]+1
        elif(lowerCaseWord.startswith('b',0)): 
            listb[1] = listb[1]+1      
        elif(lowerCaseWord.startswith('c',0)): 
            listc[1] = listc[1]+1  
        elif(lowerCaseWord.startswith('d',0)): 
            listd[1] = listd[1]+1   
        elif(lowerCaseWord.startswith('e',0)): 
            liste[1] = liste[1]+1      
        elif(lowerCaseWord.startswith('f',0)): 
            listf[1] = listf[1]+1  
        elif(lowerCaseWord.startswith('g',0)): 
            listg[1] = listg[1]+1 
        elif(lowerCaseWord.startswith('h',0)): 
            listh[1] = listh[1]+1      
        elif(lowerCaseWord.startswith('i',0)): 
            listi[1] = listi[1]+1  
        elif(lowerCaseWord.startswith('j',0)): 
            listj[1] = listj[1]+1   
        elif(lowerCaseWord.startswith('k',0)): 
            listk[1] = listk[1]+1      
        elif(lowerCaseWord.startswith('l',0)): 
            listl[1] = listl[1]+1  
        elif(lowerCaseWord.startswith('m',0)): 
            listm[1] = listm[1]+1
        elif(lowerCaseWord.startswith('n',0)): 
            listn[1] = listn[1]+1      
        elif(lowerCaseWord.startswith('o',0)): 
            listo[1] = listo[1]+1  
        elif(lowerCaseWord.startswith('p',0)): 
            listp[1] = listp[1]+1   
        elif(lowerCaseWord.startswith('q',0)): 
            listq[1] = listq[1]+1      
        elif(lowerCaseWord.startswith('r',0)): 
            listr[1] = listr[1]+1  
        elif(lowerCaseWord.startswith('s',0)): 
            lists[1] = lists[1]+1
        elif(lowerCaseWord.startswith('t',0)): 
            listt[1] = listt[1]+1      
        elif(lowerCaseWord.startswith('u',0)): 
            listu[1] = listu[1]+1  
        elif(lowerCaseWord.startswith('v',0)): 
            listv[1] = listv[1]+1   
        elif(lowerCaseWord.startswith('w',0)): 
            listw[1] = listw[1]+1      
        elif(lowerCaseWord.startswith('x',0)): 
            listx[1] = listx[1]+1  
        elif(lowerCaseWord.startswith('y',0)): 
            listy[1] = listy[1]+1
        else:
            listz[1] = listz[1]+1
  
print "TOTAL NUMBER OF WORDS FOUND:"      
print totalWordsCounter        
print "NO. OF DISTINCT WORDS FOUND :"
print len(origDictionary)
print "\n WORDS WITH THEIR CORRESPONDING OCCURRENCES:"

#Sorting the dictionary by their keys and printing it
sortedDictionary = [x for x in origDictionary.iteritems()] 
sortedDictionary.sort(key=lambda x: x[0])
print sortedDictionary

        
    
#finding the ratio of each starting character list size against the total number of words
threeSpace[2] = 100.*threeSpace[1]/totalWordsCounter
listb[2] = 100.*listb[1]/totalWordsCounter
listc[2] = 100.*listc[1]/totalWordsCounter
listd[2] = 100.*listd[1]/totalWordsCounter
liste[2] = 100.*liste[1]/totalWordsCounter
listf[2] = 100*listf[1]/totalWordsCounter
listg[2] = 100*listg[1]/totalWordsCounter
listh[2] = 100*listh[1]/totalWordsCounter
listi[2] = 100*listi[1]/totalWordsCounter
listj[2] = 100*listj[1]/totalWordsCounter
listk[2] = 100*listk[1]/totalWordsCounter
listl[2] = 100*listl[1]/totalWordsCounter
listm[2] = 100*listm[1]/totalWordsCounter
listn[2] = 100*listn[1]/totalWordsCounter
listo[2] = 100*listo[1]/totalWordsCounter
listp[2] = 100*listp[1]/totalWordsCounter
listq[2] = 100*listq[1]/totalWordsCounter
listr[2] = 100*listr[1]/totalWordsCounter
lists[2] = 100*lists[1]/totalWordsCounter
listt[2] = 100*listt[1]/totalWordsCounter
listu[2] = 100*listu[1]/totalWordsCounter
listv[2] = 100*listv[1]/totalWordsCounter
listw[2] = 100*listw[1]/totalWordsCounter
listx[2] = 100*listx[1]/totalWordsCounter
listy[2] = 100*listy[1]/totalWordsCounter
listz[2] = 100*listz[1]/totalWordsCounter

print "\n ALPHABET,No. OF OCCURRENCES, % OF OCCURRENCE"
print threeSpace,"\n",listb,"\n",listc,"\n",listd,"\n",liste,"\n",listf,"\n",listg,"\n",listh,"\n",listi,"\n",listj,"\n",listk,"\n",listl,"\n",listm,"\n",listn,"\n",listo,"\n",listp,"\n",listq,"\n",listr,"\n",lists,"\n",listt,"\n",listu,"\n",listv,"\n",listw,"\n",listx,"\n",listy,"\n",listz

#plotting the graph using the sorted dictionary
 
 
