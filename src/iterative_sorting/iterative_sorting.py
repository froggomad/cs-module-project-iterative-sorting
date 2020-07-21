# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # ### MARK TODO FIXME Maybe -1 is not necessary
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        smallest_value = arr[cur_index]
        
        for index in range(cur_index, len(arr)):
            if arr[index] < smallest_value:
                smallest_value = arr[index]
                smallest_index = index
        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr): 
    count = len(arr) 
  
    # Loop through each index except the last one
    for i in range(count-1):
        #length - current index - 1
        #swap positions if there's a mismatch
        for index in range(0, count - i - 1):
            if arr[index] > arr[index+1] : 
                arr[index], arr[index+1] = arr[index+1], arr[index]
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here    
    if arr != None:
        if maximum == None:
            maximum = len(arr)
        #make an array of 0's 1 over the max
        max = maximum+1
        buckets = [0 for i in range(max)]
        
        #fill the buckets given rules
        for num in arr:
            if num < 0:
                return "Error, negative numbers not allowed in Count Sort"
            if num > maximum:
                print("Over Max, don't include")
            else:
                buckets[num] += 1
        print(buckets)
        #track each array position
        i=0
        #iterate up to the max, filling each position with a sorted value
        for bucket in range(max-1):
                arr[i] = bucket
                i += 1
        return arr
import random
arr4 = random.sample(range(200), 50)
arr = [1,3,3,4,5,6,7,3,4,5,6,7]
print(sorted(arr4))
arr = counting_sort(arr4)

print(arr)