import time

# Bubble Sort Function
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop if already sorted
        if not swapped:
            break

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Time
start_time = time.perf_counter()

# Sorting
bubble_sort(arr)

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

