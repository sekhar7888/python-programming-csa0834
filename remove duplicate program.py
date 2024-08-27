def remove_duplicates(arr):
    
    element_count = {}
    for num in arr:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    
    unique_elements = [num for num in arr if element_count[num] == 1]
    
    return unique_elements


array = [15, 14, 25, 14, 32, 14, 31]


result = remove_duplicates(array)

print("Array after removing duplicates entirely:", result)
