import bisect
def longest_subarray_sum_at_most_k(arr,k):
    pref_sum =  0
    max_len = 0

    pref_list = [(0,-1)]

    for i,num in enumerate(arr):
        pref_sum += num
        target = pref_sum - k

        idx = bisect.bisect_left(pref_list,(target, float('-inf')))

        #to check the idx is in valid in prev list to retrieve else ind error
        if idx < len(pref_list):
            prev_idx = pref_list[idx][1]
            max_len = max(max_len, i-prev_idx)
        
        bisect.insort(pref_list,(pref_sum,i))
    return max_len

nums = [3, -2, 5, -1]
k = 4
print(longest_subarray_sum_at_most_k(nums, k))
