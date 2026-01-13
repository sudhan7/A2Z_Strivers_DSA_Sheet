"""
Bubble sort
push the max to the last
by adjacent swap

"""

def bubbleSort(nums):
    for i in range(len(nums)-1,-1,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [7, 4, 1, 5, 3]
print(bubbleSort(nums))

#time complexity
#O(N^2)