def merge(left, right):
    # 返回一个合并有序的数组
    left_idx, right_idx = 0, 0
    res = []
    # 当左边的索引小于左边数组的长度和右边的索引小于右边数组的长度
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            # 将左边的元素添加到数组中
            res.append(left[left_idx])
            # 索引进行加1
            left_idx += 1
        else:
            # 将右边的元素添加到数组中
            res.append(right[right_idx])
            right_idx += 1
    # 将未添加到数组中的元素添加到数组中
    res += left[left_idx:]
    res += right[right_idx:]
    return res


def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2  # 数组的中间位置
    # 左边的数组
    left = mergeSort(nums[:mid])
    # 右边的数组
    right = mergeSort(nums[mid:])
    return merge(left=left, right=right)


nums = [3, 443, 5676, 23, 7686, 3, 5, 76, 8, 9, 0, 1, 2, 4, 6]
test = mergeSort(nums)
print(test)