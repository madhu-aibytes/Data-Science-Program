
#This  is a python code to perform binary search on a 2D matrix to find a target value.

def search_2d_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

matrix = []
rows = int(input("Enter number of rows in the matrix: "))
cols = int(input("Enter number of columns in the matrix: "))
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i}, {j}): "))
        row.append(element)
    matrix.append(row)
print("The 2D matrix is:")
for row in matrix:
    print(row)
target_value = int(input("Enter the target value to search for: "))
found = search_2d_matrix(matrix, target_value)
if found:
    print(f"Target value {target_value} found in the matrix.")
else:
    print(f"Target value {target_value} not found in the matrix.")
    
    
    
    
    
""" Perform binary search on a 2D matrix to find the target value.
    Parameters:
    matrix (list of list): The 2D matrix to search through.     
    target: The value to search for.
    Returns: 
    bool: True if the target is found, otherwise False."""
    