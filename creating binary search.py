def binary_search(arr, target):
    
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

                                
        if arr[mid] == target:               # Check if target is present at mid
            return mid
        
        elif arr[mid] < target:              # If target is greater, ignore left half
            left = mid + 1
        
        else:                               # If target is smaller, ignore right half
            right = mid - 1

  
    return -1                                # Target was not found in the array


array = []
n = int(input("Enter number of elements in the sorted array: "))
for i in range(n):
    element = int(input("Enter element: "))
    array.append(element)
target_value = int(input("Enter the target value to search for: "))
result_index = binary_search(array, target_value)
if result_index != -1:
    print(f"Target value {target_value} found at index: {result_index}")
else:
    print(f"Target value {target_value} not found in the array.")
    


    """ Perform binary search on the given sorted array to find the target value.  
    Parameters:
    arr (list): The sorted list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1."""
    