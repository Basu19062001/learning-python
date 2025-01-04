arr = [1,2,3,6,8,7,9,4]
n = len(arr) + 1

expected_sum = n *(n+1) // 2
actual_sum = sum(arr)

missing_number = expected_sum - actual_sum
print(f"Missing Number is : {missing_number}")
