import time

# Insertion Sort Function
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Time
start_time = time.perf_counter()

# Sorting
insertion_sort(arr)

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
print("Best Case   : O(n)")
print("Average Case: O(n^2)")
print("Worst Case  : O(n^2)")
print("Space Complexity: O(1)")