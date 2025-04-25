# Raphson
import random
import time

# Generating 1000 random sensor data
sensor_data = [random.randint(0, 10000) for _ in range(1000)]

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Testing
data = sensor_data.copy()

print("Original first 10 sensor readings:", data[:10])

# Bubble Sort
start = time.time()
bubble_sorted = data.copy()
bubble_sort(bubble_sorted)
print("\nBubble Sort took", time.time() - start, "seconds.")

# Merge Sort
start = time.time()
merge_sorted = data.copy()
merge_sort(merge_sorted)
print("Merge Sort took", time.time() - start, "seconds.")

# Quick Sort
start = time.time()
quick_sorted = quick_sort(data.copy())
print("Quick Sort took", time.time() - start, "seconds.")

# Searching after sorting
target = sensor_data[random.randint(0, 999)]

# Linear Search
start = time.time()
linear_result = linear_search(sensor_data, target)
print("\nLinear Search took", time.time() - start, "seconds.")

# Binary Search (on sorted data)
start = time.time()
binary_result = binary_search(merge_sorted, target)
print("Binary Search took", time.time() - start, "seconds.")