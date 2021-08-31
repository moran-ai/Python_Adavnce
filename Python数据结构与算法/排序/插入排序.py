def insertSort(nums):
    n = len(nums)
    for i in range(n-1):
        curNum = nums[i+1]  # 无序区的第一个元素
        idx = i  # 有序区的最后一个元素的索引
        while nums[idx] > curNum and idx >= 0:
            nums[idx+1] = nums[idx]  # 把有序区的元素往后移动
            idx -= 1  # 指针向前移动，从后往前遍历有序区
        nums[idx+1] = curNum


test = [4, 51, 27, 8, 90, 2, 31]
insertSort(test)
print(test)