from collections import Counter

string = "Programming"
counter = Counter(string)

duplicates = [char for char, count in counter.items() if count > 1]
print(duplicates)