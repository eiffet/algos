
import sort.insert_sort.v2 as insert_sort

arr = [7,1,9,4,-1,0]

insert_sort.sort(arr)

print "result: {}".format(arr)
print "# swaps: {}".format(insert_sort.swaps)
print "micros: {}".format(insert_sort.micros)

