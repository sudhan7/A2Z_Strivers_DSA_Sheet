def two_sum(arr,target):
    ind = {}
    for i in range(len(arr)):
        sup = target - arr[i]
        if sup in ind and i!=ind[sup]:
            return [ind[sup], i]
        else:
            ind[arr[i]] = i 

target = 13
arr = [2,6,5,8,11]
print(two_sum(arr,target))