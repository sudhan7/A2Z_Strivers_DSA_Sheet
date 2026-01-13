def merged_interval(arr):
    arr.sort()
    merged = []

    for interval in arr:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

interval = [[1,3],[2,6],[8,10],[15,18]]
print(merged_interval(interval))