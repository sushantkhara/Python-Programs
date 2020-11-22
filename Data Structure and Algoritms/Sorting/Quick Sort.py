def quickSort(alist):
   quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist, first, splitpoint-1)
       quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
   pivot_value = alist[first]
   left_mark = first+1
   rightmark = last

   done = False
   while not done:

       while left_mark <= rightmark and alist[left_mark] <= pivot_value:
           left_mark = left_mark + 1

       while alist[rightmark] >= pivot_value and rightmark >= left_mark:
           rightmark = rightmark -1

       if rightmark < left_mark:
           done = True
       else:
           temp = alist[left_mark]
           alist[left_mark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)
