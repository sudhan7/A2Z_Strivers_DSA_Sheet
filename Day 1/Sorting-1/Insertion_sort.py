"""
Selection sort

take an element and place
it in correct order
"""

def insertion_Sort(nums):
    # For every element in the array 
    for i in range(1,len(nums)):
        key = nums[i] # Current element as key 
        j = i-1

        # Shift elements that are greater than key by one position
        while j>= 0 and nums[j] > key:
            nums[j+1] = nums[j] 
            j-=1

        nums[j+1] = key # Insert key at correct position
    
    return nums

nums = [7, 4, 1, 5, 3]
print(insertion_Sort(nums))

#Time complexity
#O(N^2)