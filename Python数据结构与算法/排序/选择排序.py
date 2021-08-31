def selectSort(nums):
    n = len(nums)
    for i in range(n-1):
        # 找出无序区中最小的元素
        min_index = i  # 无序区中最小元素的索引
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index=j

        # 最小元素和有序区中的后一个元素进行位置的交换
        nums[i], nums[min_index] = nums[min_index], nums[i]
        print(nums)

lst = [6,4,3,1,2]
selectSort(lst)
