def bubblesort(nums):
    for i in range(len(nums)-1):
        flag = False  # 用来记录是否进行了数组的交换
        for idx in range(0, len(nums)-1-i):
            if nums[idx] > nums[idx+1]:
                nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
                flag = True # 如果执行了，则代表数组进行了交换
            print(f'第{i+1}趟排序', nums)
        if not flag:
            break

# test = [6, 5, 4, 3, 2, 1]
test = [1,2,3,4,5,6]
bubblesort(test)

