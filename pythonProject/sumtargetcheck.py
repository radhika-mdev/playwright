nums = [3,2,4]
target = 6
lookup={}


def twosum( nums, target):
    lookup = {}
    for cnt, num in enumerate(nums):
        if target - num in lookup:
            return lookup[target-num], cnt
        lookup[num] = cnt

print(twosum(nums,target))