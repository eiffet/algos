
import sys, os
from datetime import datetime

def current_micro():
    return datetime.now().microsecond

def loPivot(arr, lo, hi):
    return lo

def hiPivot(arr, lo, hi):
    return hi

def midPivot(arr, lo, hi):
    return lo + ((hi - lo + 1) / 2)

def medianPivot(arr, lo, hi):
    mid = lo + ((hi - lo + 1) / 2)
    loval = arr[lo]
    hival = arr[hi]
    midval = arr[mid]
    if loval <= midval <= hival or hival <= midval <= loval:
        return mid
    elif loval <= hival <= midval or midval <= hival <= loval:
        return hi
    elif midval <= loval <= hival or hival <= loval <= midval:
        return lo

pivotmethod = sys.argv[1]

choosePivot = loPivot
if pivotmethod == 'lo':
    choosePivot = loPivot
elif pivotmethod == 'hi':
    choosePivot = hiPivot
elif pivotmethod == 'mid':
    choosePivot = midPivot
elif pivotmethod == 'median':
    choosePivot = medianPivot
else:
    exit("Bad pivot method {0}".format(pivotmethod))

items = [int(x) for x in sys.argv[2:]]

partition_calls = 0
swap_calls = 0

def swap(x, y):
    global swap_calls
    swap_calls += 1
    return (y, x)

def partition(a, lo, hi):
    global partition_calls
    partition_calls += 1
    pivotindex = choosePivot(a, lo, hi)
    pivotvalue = a[pivotindex]
    (a[pivotindex], a[hi]) = swap(a[pivotindex], a[hi])
    storeindex = lo
    for i in xrange(lo, hi):
        if a[i] < pivotvalue:
            (a[storeindex], a[i]) = swap(a[storeindex], a[i])
            storeindex += 1
    (a[storeindex], a[hi]) = swap(a[storeindex], a[hi])
    return storeindex

def quicksort(a, lo, hi): 
    if lo < hi:
        p = partition(a, lo, hi)
        quicksort(a, lo, p-1)
        quicksort(a, p+1, hi)

start_time = current_micro()
quicksort(items, 0, len(items)-1)
end_time = current_micro()
print items
print "Used pivotmethod {0}".format(pivotmethod)
print "Called partition() {0} times".format(partition_calls)
print "Called swap() {0} times".format(swap_calls)
print "total time: {0} micros".format(end_time - start_time)
