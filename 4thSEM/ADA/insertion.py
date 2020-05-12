

import time
def insertionSort(arr1):
    arr = arr1.copy()
    for i in range(1, len(arr) - 1):
        ele = arr[i]
        j = i - 1
        while j > -1 and arr[j] > ele:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ele
    return arr

arr = [int(i) for i in input('Enter the numbers to be sorted : ').split()]
st1 = time.process_time()
tt = time.process_time() - st1

print('Sorted array :')
print(insertionSort(arr))
print("Time taken to sort the array using insertion sort : " + str(tt))
