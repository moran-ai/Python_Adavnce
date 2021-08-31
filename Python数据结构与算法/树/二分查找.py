# 二分查找 递归版
def binary_search(nums, target, left, right):
    """
    nums: 待查找的数组，要求是升序的
    target:带查找的数字
    left:区间的左边索引
    right: 区间的右边索引
    """
    # 递归结束的条件
    if left > right:
        return False
    # 找中间值
    mid = (left + right) // 2
    # print(mid)
    # 判断中间值是否等于目标值
    if nums[mid] == target:
        return True
    # 如果中间值小于目标值,说明目标值在目标值的右边
    if nums[mid] < target:
        return binary_search(nums=nums, target=target, left=mid + 1, right=right)
    return binary_search(nums=nums, target=target, left=left, right=mid-1)


nums = [1, 4, 5, 23, 4, 6, 2, 54, 6, 45, 7]
print(binary_search(nums, 1, 0, len(nums)-1))
print(binary_search(nums, 99, 0, len(nums)-1))
