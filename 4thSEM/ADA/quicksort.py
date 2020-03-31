import time
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if low < high:
        part = partition(arr, low, high)
        quickSort(arr, low, part-1)
        quickSort(arr, part+1, high)

arr = [int(i) for i in input("").split()]
n = len(arr)
start = time.time()
quickSort(arr, 0, n-1)
end = time.time()
print("Sorted array is: ", end="")
print(arr)
print("Time taken : " + str(end-start))
