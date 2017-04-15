

import sys
from datetime import datetime

now = datetime.now
swaps = 0
micros = 0L

def sort(arr):
    global swaps
    global micros
    swaps = 0
    start = now().microsecond
    for i in xrange(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            swaps += 1
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    end = now().microsecond
    micros = end - start
