nums = [5, 2, 7, 5, 9, 5, 3]
x = int(input())

if x in nums:
    pos = [i for i in range(0, len(nums)-1) if x==nums[i]]
    print(pos)
else:
    print("Not available")
