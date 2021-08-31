# 希尔排序，插入排序的升级
def insertSort(nums):
    n = len(nums)
    # 设定一个增量gap
    gap = n // 2
    while gap >= 1:
        # 分组
        for i in range(gap):
            # 对每一小组进行插入排序
            for j in range(i, n-gap, gap):
                curNum = nums[j+gap]  # 无序区的第一个元素
                idx = j  # 有序区的最后一个元素的索引
                while nums[idx] > curNum and idx >= 0:
                    nums[idx+gap] = nums[idx]  # 把有序区的元素往后移动
                    idx -= gap  # 指针向前移动，从后往前遍历有序区
                nums[idx+gap] = curNum
        gap //= 2  # 缩小增量


def insertSort_(nums):
    n = len(nums)
    # 设定一个增量gap
    gap = n // 2
    while gap >= 1:
        # 分组
        for i in range(gap, n):
            curNum = nums[i]
            idx = i-gap
            while idx >= 0 and curNum < nums[idx]:
                nums[idx+gap] = nums[idx]
                idx -= gap
            nums[idx+gap] = curNum
        gap //= 2  # 缩小增量


test = [4, 51, 27, 8, 90, 2, 31]
insertSort_(test)
print(test)
