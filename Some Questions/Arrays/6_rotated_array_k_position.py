arr = [1,2,3,4,5] # output [4,5,1,2,3]
k=2
rotatedArr = arr[-k:] + arr[:-k]
print(f"Rotated array is : {rotatedArr}")