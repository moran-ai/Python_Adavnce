# def test():
#     i = 1
#     a, b = 0, 1
#     while i < 25:
#         a, b = b, a + b
#         print('%8d' % b, end=' ')
#         if i % 6 == 0:
#             print()
#         i += 1
#
#
# # test()
#
#
# def fub(n):
#     a, b = 0, 1
#     for i in range(n - 1):
#         print(b)
#         a, b = b, a + b
#
#
# # fub(10)
#
# class p:
#     pass
#
#
# print('---☆☆☆--欢迎使用通讯录--☆☆☆---')
# print('1,查询联系人')
# print('2,添加联系人')
# print('3,删除联系人')
# print('4,查看现有联系人')
# print('5,修改联系人')
# print('6,退出通讯录')
# tongxun = {'小张': 132, '小刘': 133, '小连': 188, '小王': 134}
#
# while True:
#     neme = int(input('请输入你的选择：'))
#     # for ieme in list(tongxun):
#
#     if neme == 1:
#         test = input('请输入联系人名称：')
#         if test in tongxun.keys():
#             print(tongxun[test])
#         else:
#             print('你查询的联系人不存在！')
#
#     if neme == 2:
#         test = input('请输入要添加的联系人：')
#         dianhua = int(input('请输入联系人电话：'))
#         tongxun[test] = dianhua
#
#     if neme == 3:
#         test = input('请输入要删除的联系人：')
#         if test in tongxun.keys():
#             tongxun.pop(test)
#         else:
#             print('联系人不存在')
#
#     if neme == 4:
#         test = input('是否查看所有 联系人？y/n')
#         if test == 'y':
#             print(tongxun)
#
#     if neme == 5:
#         test = input('请输入要修改的联系人：')
#         dianhua = int(input('输入要修改的电话：'))
#         tongxun[test] = dianhua
#
#     if neme == 6:
#         break

# print('------指定数字转换-------')
# print(95)
# print(0b1011111)
# print(0o137)
# print(0x5f)
# print('-----为自己手机充值--------')
# a = int(input('用户手机账户有话费金额：'))
# b = int(input('请用户输入充值金额:'))
# print('当前可用余额：', a + b)
# print('------计算能量的消耗------  ')
# a = int(input('请输入您当天的步数：'))
# b = 28
# print('今天共消耗卡路里', a * b, '即', a * b * 0.001)
# print('---------预测未来子女身高-------')
# a = int(input('请输入父亲身高：'))
# b = int(input('请输入母亲身高：'))
# print('预测子女的身高为', (a + b) * 0.54, 'cm')

#
# def read_single_spectrum(file_path):
#     # 读取单独的光谱文件
#
#     f = open(file_path, "r+", encoding='utf-8')
#     data_file = []
#     x_axis_file = []
#
#     for line in f:
#         x_axis_file.append(float(line.split()[0]))
#         data_file.append(float(line.split()[-1]))
#
#     f.close()
#
#     return x_axis_file, data_file
#
#
# read_single_spectrum('100mMspectrum_total(1).xlsx')



