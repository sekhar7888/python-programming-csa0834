from collections import Counter
import statistics

def calculate_mean(arr):
    return sum(arr) / len(arr)

def calculate_median(arr):
    arr.sort()  # Sort the array
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]

def calculate_mode(arr):
    # Using Counter to count the frequency of elements
    count = Counter(arr)
    max_count = max(count.values())
    mode = [k for k, v in count.items() if v == max_count]
    
    # If every number appears only once, there's no mode
    if len(mode) == len(arr):
        return "No mode"
    
    return mode

# Example usage
array = [16, 18, 27, 16, 23, 21, 19]  # You can change this input

mean = calculate_mean(array)
median = calculate_median(array)
mode = calculate_mode(array)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
