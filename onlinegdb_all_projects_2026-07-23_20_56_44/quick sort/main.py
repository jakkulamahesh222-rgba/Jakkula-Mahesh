import time

# Partition Function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quick Sort Function
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Time
start_time = time.perf_counter()

# Sorting
quick_sort(arr, 0, len(arr) - 1)

# End Time
end_time = time.perf_counter()

# Output
print("\nSorted Array:")
print(arr)

# Execution Time
execution_time = end_time - start_time
print(f"\nExecution Time: {execution_time:.8f} seconds")

# Time Complexity
print("\nTime Complexity:")
print("Best Case   : O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case  : O(n^2)")
print("Space Complexity: O(log n)")
