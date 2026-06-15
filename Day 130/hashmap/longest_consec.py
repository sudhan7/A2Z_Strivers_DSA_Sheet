def longest_consec(nums):
    numset = set(nums)
    longest = 0

    for num in nums:
        if (num - 1) not in numset:
            length = 0
            while (num + length) in numset:
                length += 1
        longest = max(longest, length)
    return longest

nums = [100,4,200,1,3,2]
print(longest_consec(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(longest_consec(nums))