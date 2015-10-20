import plotly.plotly as py
import plotly.graph_objs as go
import time
import random

#This program takes randomly generated arrays, sorts them with bubble and merge sort, times the sorting process, and graphs it

#enter random array lengths here to be sorted and timed
sizearray = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
n = len(sizearray)

#Generate random array of (size) from zero to (numhigh)
def generaterandomarray(size, numhigh):
    listofnumbers = []
    for i in range (0, size):
        listofnumbers.append(random.randint(0, numhigh))
    return listofnumbers

#Bubble Sort
def bubblesort(alist):
    for i in range(len(alist)-1,0,-1):
        for i in range(i):
            if alist[i]>alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

#Merge Sort
def mergesort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i,j,k =0,0,0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

#Print graphs to Plotly
def printgraphs(a,b,c,d):
    trace0 = go.Scatter(x=a, y=b)
    trace1 = go.Scatter(x=c, y=d)
    data = [trace0, trace1]
    unique_url = py.plot(data, filename = 'basic-line')

#Use this function to only print one of the data sets to Ploty
def onegraph(a,b):
    trace0 = go.Scatter(x=a, y=b)
    data = [trace0]
    unique_url = py.plot(data, filename = 'basic-line')

grapharraya, grapharrayb, grapharrayc, grapharrayd, arr = [], [], [], [], []
totalbubbletime, totalmergetime = 0,0       #running total time
repeat = 50                                 #how times to repeat for an average
for i in range(0,n):                        #for each element in sizearray
    for j in (0,repeat):
        arr = generaterandomarray(sizearray[i], 100000) #generate random array of that size
        arr2 = arr                          #assign it to another array for the second sorting algorithm
        startbubble_time = time.time()
        bubblesort(arr)
        bubbletime = (startbubble_time - time.time())
        totalbubbletime += bubbletime

        startmerge_time = time.time()
        mergesort(arr2)
        mergetime = (startmerge_time - time.time())
        totalmergetime += mergetime

    grapharraya.append(sizearray[i])
    grapharrayb.append(abs(totalbubbletime/repeat))
    grapharrayc.append(sizearray[i])
    grapharrayd.append(abs(totalmergetime/repeat))

print printgraphs(grapharraya, grapharrayb, grapharrayc, grapharrayd)
#print onegraph(grapharrayc, grapharrayd)





