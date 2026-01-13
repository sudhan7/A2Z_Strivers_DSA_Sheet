def selectionSort(nums):
    for i in range(len(nums)):
        mini = nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] < mini:
                mini = nums[j]
                nums[j],nums[i] = nums[i], nums[j]
    return nums
            

nums = [7, 4, 1, 5, 3]
print(selectionSort(nums))

"""
Selection sort
select the min value and swap to the front
"""
#time complexity 
#O(n^2)
