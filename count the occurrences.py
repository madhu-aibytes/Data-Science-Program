def count_occurrences(arr, target):
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count
array = []
n = int(input("Enter number of elements in the array: "))
for i in range(n):
    element = int(input("Enter element: "))
    array.append(element)
target_value = int(input("Enter the target value to count occurrences for: "))
occurrences = count_occurrences(array, target_value)
print(f"Target value {target_value} occurs {occurrences} times in the array.")