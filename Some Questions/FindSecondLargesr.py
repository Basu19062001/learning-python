
def findSecondLargest(nums: list[int]) -> int:
  nums.sort(reverse=True)
  return nums[1] if len(nums) > 1 else None

print(findSecondLargest([3]))