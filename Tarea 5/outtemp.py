def permutation(nums):
  ans = None
  i = len(nums) - 2
  while i >= 0 and nums[i] >= nums[i + 1]:
    i -= 1
  if i == -1:
    ans = False
  else:
    j = i + 1
    while j < len(nums) and nums[j] > nums[i]:
      j += 1
    j -= 1

    nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1:] = nums[i + 1:][::-1]
    ans = True
  
  return ans

nums = [1, 2, 3, 4, 5]
print(nums)

permutation(nums)

print(nums)

permutation(nums)

print(nums)