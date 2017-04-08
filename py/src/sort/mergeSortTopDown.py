
import sys
from datetime import datetime

merge_appends = 0
splits = 0
split_appends = 0

def current_micro():
    return datetime.now().microsecond

def merge(a, b):
    global merge_appends
    result = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            result.append(a[0])
            merge_appends += 1
            a.pop(0)
        else:
            result.append(b[0])
            merge_appends += 1
            b.pop(0)
    while len(a) > 0:
        result.append(a[0])
        merge_appends += 1
        a.pop(0)
    while len(b) > 0:
        result.append(b[0])
        merge_appends += 1
        b.pop(0)
    return result

def mergeSort(data):
    global splits
    global split_appends
    if len(data) <= 1:
        return data
    a = []
    b = []
    mid = len(data) / 2
    for x in xrange(0, mid):
        a.append(data[x])
        split_appends += 1
    for y in xrange(mid, len(data)):
        b.append(data[y])
        split_appends += 1
    splits += 1
    a = mergeSort(a)
    b = mergeSort(b)
    return merge(a, b)

items = [int(x) for x in sys.argv[1:]]
start_time = current_micro()
print mergeSort(items)
end_time = current_micro()
print "splits: {0}".format(splits)
print "split appends: {0}".format(split_appends)
print "merge appends: {0}".format(merge_appends)
print "total time: {0} micros".format(end_time - start_time)
