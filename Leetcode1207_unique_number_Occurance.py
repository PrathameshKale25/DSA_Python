def unique_number_occurrence(arr):
    # Count occurrences of each element
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    # Check if all occurrence counts are unique
    occurrences = list(freq.values())
    return len(occurrences) == len(set(occurrences))

# Test array
arr = [1, 2, 1, 2, 1, 3, 1, 4, 1, 3, 1, 4]
print(unique_number_occurrence(arr))  # Output: True or False based on uniqueness of occurrences
