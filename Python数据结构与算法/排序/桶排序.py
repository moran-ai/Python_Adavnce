def bucketSort(nums, size=5):
    # 根据数组的最大值和最小值确定桶的数量
    maxVal = max(nums)
    minVal = min(nums)
    buckeCount = (maxVal - minVal) // size + 1  # 桶的数量
    buckets = [[] for _ in range(buckeCount)]  # 申请桶
    for num in nums:
        idx = (num - minVal) // size  # 值num的所在位置，idx为该值的索引
        n = len(buckets[idx])  # 当前桶的元素
        i = 0
        # 找到第一个比num大的元素
        while i < n and buckets[idx][i] < num:
            i += 1
        buckets[idx].insert(i, num)
    print(buckets)

    # 合并桶
    nums.clear()
    for bucket in buckets:
        nums.extend(bucket)


test = [4, 51, 27, 8, 90, 2, 31]
bucketSort(test)
print(test)
