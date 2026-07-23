import time

# Selection Sort Function
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Time
start_time = time.perf_counter()

# Sorting
selection_sort(arr)

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
print("Best Case   : O(n^2)")
print("Average Case: O(n^2)")
print("Worst Case  : O(n^2)")
print("Space Complexity: O(1)")