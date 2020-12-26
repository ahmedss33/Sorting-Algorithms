import random
import time

############################# INSERTION SORT - SORTED ########################
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue


##############################################################################

############################## MERGE SORT - SORTED ###########################
def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
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
    #print("Merging ",alist)
##############################################################################

##################### IN-PLACE QUICK SORT - SORTED ###########################
def quickSort(items):

    def sort(lst, l, r):
        # base case
        if r <= l:
            return

        # choose random pivot
        pivot_index = random.randint(l, r)

        # move pivot to first index
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        # partition
        i = l
        for j in range(l+1, r+1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        # place pivot in proper position
        lst[i], lst[l] = lst[l], lst[i]

        # sort left and right partitions
        sort(lst, l, i-1)
        sort(lst, i+1, r)

    if items is None or len(items) < 2:
        return

    sort(items, 0, len(items) - 1)
################################################################################

##################### MODIFIED QUICK SORT - SORTED ###############################
def quickSortM(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotindex = median(alist, first, last, (first + last) // 2)
   alist[first], alist[pivotindex] = alist[pivotindex], alist[first]
   pivotvalue = alist[first]

   leftmark = first
   rightmark = last
   
   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = pivotvalue
   alist[alist.index(pivotvalue)] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def median(a, i, j, k):
  if a[i] < a[j]:
    return j if a[j] < a[k] else k
  else:
    return i if a[i] < a[k] else k
################################################################################
alist = []
print("Please enter the random number range to sort")
new=input()
print('\n-----------------------------------------------------------------------')

numbers = random.sample(range(1, 100000), int(new))
sort=sorted(numbers)
alist = sort

####################### CALLING INSERTION SORT - SORTED ##########################
print('Sorting using Insertion Sort\n')
t1=time.time()
insertionSort(alist)
t2=time.time()
print(alist)

print ("The algorithm took " + str((t2-t1) * 1000)  + " ms of time.")
print('\n-----------------------------------------------------------------------')

########################### CALLING MERGE SORT - SORTED ##########################
print('Sorting using Merge Sort\n')
t3=time.time()
mergeSort(alist)
t4=time.time()
print('Using the same Dataset...')
print ("The algorithm took " + str((t4-t3) * 1000)  + " ms of time.")
print('\n-----------------------------------------------------------------------')
################## CALLING IN-PLACE QUICK SORT - SORTED ##########################
print('Sorting using In-Place Quick Sort\n')
t5=time.time()
quickSort(numbers)
t6=time.time()
print('Using the same Dataset...')
print ("The algorithm took " + str((t6-t5) * 1000)  + " ms of time.")
print('\n-----------------------------------------------------------------------')
##################### CALLING MODIFIED QUICK SORT - SORTED ##############################
print('Sorting using Modified Quick Sort\n')
if(int(new)<=10):
    print("Since number of elements to be sorted is lesser than 10, insertion sort needs to be implemented")
    t7=time.time()
    insertionSort(alist)
else:
    print("Since number of elements to be sorted is greater than 10, quick sort needs to be implemented")
    t7=time.time()
    quickSortM(alist)
t8=time.time()
print('Using the same Dataset...')

print ("The algorithm took " + str((t8-t7) * 1000)  + " ms of time.")
print('\n-----------------------------------------------------------------------')