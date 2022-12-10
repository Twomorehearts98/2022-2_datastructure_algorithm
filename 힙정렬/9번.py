def swap(arr, a, b):
    tmp = arr[a]
    arr[a]= arr[b]
    arr[b] = tmp

def heapify(arr, here, size):
    left = here*2+1
    right = here*2+2
    max = here
    if(left<size and arr[left]>arr[max]):
        max = left
    if(right<size and arr[right]>arr[max]):
        max = right
    if(max != here):
        swap(arr, here, max)
        heapify(arr, max, size)

def buildheap(arr, size):
    for i in range(size//2-1, -1, -1):
        heapify(arr, i, size)
        for j in range(0, size):
            print(arr[j], end=" ")
        print()
        print()

def heapsort(arr, size):
    buildheap(arr, size)
    for treesize in range(size-1, -1, -1):
        swap(arr, 0, treesize)
        heapify(arr, 0, treesize)

def printarray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()

arr = [5, 3, 4, 1, 6, 10]

size = len(arr)

heapsort(arr, size)
printarray(arr, size)