def linear_search(arr, target):

    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


array = []
n = int(input("Enter number of elements in the array: "))
for i in range(n):
    element = int(input("Enter element: "))
    array.append(element)
target_value = int(input("Enter the target value to search for: "))
result_index = linear_search(array, target_value)
if result_index != -1:
    print(f"Target value {target_value} found at index: {result_index}")
else:
    print(f"Target value {target_value} not found in the array.")
    
    
    
""" Perform a linear search on the given array to find the target value.

    Parameters:
    arr (list): The list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1."""



    
    
    