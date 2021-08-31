filename = 'student.txt'


def main():
    while True:
        menm()
        choice = int(input('请选择'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break  # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menm():
    print('............................................学生信息管理系统........................................')
    print('.............................................功能菜单..............................................')
    print('。。。。。。。。。。。。。。。。。。。。。。。。。1. 录入学生信息')
    print('。。。。。。。。。。。。。。。。。。。。。。。。。2.查找学生信息')
    print('。。。。。。。。。。。。。。。。。。。。。。。。。3. 删除学生信息')
    print('。。。。。。。。。。。。。。。。。。。。。。。。。4.修改学生信息')
    print('。。。。。。。。。。。。。。。。。。。。。。。。。5.        排序')
    print('。。。。。。。。。。。。。。。。。。。。。。。。。6.统计学生总人数')
    print('。。。。。。。。。。。。。。。。。。。。。。。。。7.显示所有学生信息')
    print('。。。。。。。。。。。。。。。。。。。。。。。。。0.退出')


def insert():
    student_list = []
    while True:
        id = input('请输入ID(如1001):')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入Python成绩：'))
            java = int(input('请输入Java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('是否继续添加？y/n')
        if answer == 'y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完毕！！！')


def save(list):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in list:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    pass


def delete():
    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


#
# if __name__ == '__main__':
#     main()


class a:
    # def __new__(cls, *args, **kwargs):
    #     return a

    def c(self):
        print('ok')


d = a()
d.c()
