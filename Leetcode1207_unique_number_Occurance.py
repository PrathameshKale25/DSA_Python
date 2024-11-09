def unique_number_occurrence(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1 
    occurrences = list(freq.values())
    return len(occurrences) == len(set(occurrences))
arr = [1, 2, 1, 2, 1, 3, 1, 4, 1, 3, 1, 4]
print(unique_number_occurrence(arr))  
