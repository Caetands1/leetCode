nums = [2,5,5,11]
target = 10

for i in nums:
    for x in range(1,len(nums)):
        if i + nums[x] == target: 
            if nums.index(i) == x:
                continue
            else:
                print(nums.index(i), x)