def binary_search(arr:list, target: int) -> int:
  start = 0
  end = len(arr) -1
  
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return -1


arr = [2,4,6,8,9,3,5,6,8,83,2,4,5,78,2]
print(binary_search(arr, 5))