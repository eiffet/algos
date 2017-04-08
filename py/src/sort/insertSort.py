
import sys
from datetime import datetime

def current_micro():
    return datetime.now().microsecond

print 'Arguments: ', str(sys.argv)
print '#Args: ', len(sys.argv)

items = [int(x) for x in sys.argv[1:]]

swap_calls = 0

start_time = current_micro()
for i in xrange(1, len(items)):
    j = i
    while j > 0 and items[j-1] > items[j]:
        swap_calls += 1
        (items[j], items[j-1]) = (items[j-1], items[j])
        j = j - 1
end_time = current_micro()

print items
print "Called swap() {0} times".format(swap_calls)
print "total time: {0} micros".format(end_time - start_time)
