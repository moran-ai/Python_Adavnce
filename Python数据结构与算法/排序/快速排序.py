def quickSort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    piovt = nums[0]  # 基准值
    left = []
    right = []
    for i in range(1, n):
        if nums[i] < piovt:
            left.append(nums[i])
        else:
            right.append(nums[i])
    print(left, piovt, right)
    print('-'*60)
    return quickSort(left) + [piovt] + quickSort(right)


def partition(nums, left, right):
    pivot = nums[left]
    while left < right:
        # 挖坑，填坑
        # 当左边的数小于右边的数，并且右边的数大于基准值时索引左移
        while left < right and nums[right] > pivot:
            right -= 1
        nums[left] = nums[right]
        # 当左边的值小于右边的值，并且左边的值小于等于基准值时
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left] 
    nums[left] = pivot  # 索引和基准值重合
    return left


def quickSort1(nums, left, right):
    if left >= right:
        return 
    # 分区
    pivot_idx = partition(nums, left=left, right=right)
    # 左边的区域 left  -- > pivot_idx - 1
    quickSort1(nums, left, pivot_idx - 1)
    # 右边的区域 pivot_idx+1 ---> idx
    quickSort1(nums, pivot_idx+1, right=right)


nums = [3, 443, 5676, 23, 7686, 3, 5, 76, 8, 9, 0, 1, 2, 4, 6]
quickSort1(nums, 0, len(nums)-1)
print(nums)
