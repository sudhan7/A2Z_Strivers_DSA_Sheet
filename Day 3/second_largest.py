def second_largest(arr):
    lar = max(arr)
    sec_lar = arr[0]

    for num in arr:
        if num < lar and num > sec_lar:
            sec_lar = num
    
    return sec_lar

arr = [1, 2, 4, 7, 7, 5]  
print(second_largest(arr))