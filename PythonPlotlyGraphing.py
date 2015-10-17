import plotly.plotly as py
import plotly.graph_objs as go
import time
import random

#This program takes randomly generated arrays, sorts them with bubble and merge sort, times the sorting process, and graphs it

#enter random array lengths here to be sorted and timed
sizearray = [5, 10, 15, 25, 35, 45, 50, 75, 100, 250, 500, 750, 1000, 1500]
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

#Performs bubble sort and times the operation
def callBubble():
    grapharrayA, grapharrayB, arr = [], [], []
    for i in range(0,n-1):
        arr = generaterandomarray(sizearray[i], 10000)
        start_time = time.time()
        bubblesort(arr)
        total_time = (start_time - time.time())
        grapharrayA.append(sizearray[i])
        grapharrayB.append(round(abs(total_time), 5))
    return grapharrayA, grapharrayB

#Performs merge sort and times the operation
def callMerge():
    grapharrayC, grapharrayD, arr2 = [], [], []
    for i in range(0,n-1):
        arr2 = generaterandomarray(sizearray[i], 10000)
        start_time2 = time.time()
        mergesort(arr2)
        total_time2 = (start_time2 - time.time())
        grapharrayC.append(sizearray[i])
        grapharrayD.append(round(abs(total_time2), 5))
    return grapharrayC, grapharrayD

grapha, graphb = callBubble()
graphc, graphd = callMerge()
printgraphs(grapha, graphb, graphc, graphd)

print grapha #x axis is the size
print graphb #y axis is time
print graphc #x axis is the size
print graphd #y axis is time





