def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivot = alist[first]

   left = first+1
   right = last

   done = False
   while not done:

       while left <= right and alist[left] <= pivot:
           left = left + 1

       while alist[right] >= pivot and right >= left:
           right = right -1

       if right < left:
           done = True
       else:
           temp = alist[left]
           alist[left] = alist[right]
           alist[right] = temp

   temp = alist[first]
   alist[first] = alist[right]
   alist[right] = temp


   return right

alist = [245, 14, 65, 1, 76, 1, 100, 132]
print(alist)
quickSort(alist)
print(alist)
