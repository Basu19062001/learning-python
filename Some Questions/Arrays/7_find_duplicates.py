arr = [1,2,3,4,6,2,5,5,3,8,7,7,3,8]
duplicate = [x for x in set(arr) if arr.count(x) > 1]
min_value = min(duplicate)
max_value = max(duplicate)
print(f"Duplicate value is : {duplicate}\nMin value is : {min_value}\nMax value is : {max_value}")