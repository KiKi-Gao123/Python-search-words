info=[]  #空列表 用来存储学生信息
def show_function():
  print('------欢迎来到学生管理系统-----')
  print('------1.添加学生信息------')
  print('------2.删除学生信息------')
  print('------3.修改学生信息------')
  print('------4.查询学生信息------')
  print('------5.显示所有学生------')
  print('------6.退出系统------')


def add_stu():
    '''添加学生信息'''
    global info
    stu_name = input('请输入学生姓名:')
    stu_id = input('请输入学生学号:')
    stu_tel = input('请输入学生电话:')
    stu_sex = input('请输入学生性别:')
    for i in info:
        if stu_name == i['name']:
            print('此名字已经存在!')
            return
    info_dict = {}
    info_dict['name'] = stu_name
    info_dict['id'] = stu_id
    info_dict['tel'] = stu_tel
    info_dict['sex'] = stu_sex
    info.append(info_dict)
    print(info)

def del_stu():
    '''删除学生'''
    del_name=input('请输入要删除的学生姓名:')
    global info
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('输入有误,该学生不存在!')
    print(info)


def change_stu():
    '''修改学生信息'''
    change_name=input('请输入要修改的学生姓名:')
    global info
    for i in info:
        if change_name==i['name']:
            i['id']=input('请输入新的学号:')
            i['tel']=input('请输入新的电话号:')
            i['sex']=input('请输入新的性别:')
            break
    else:
        print('该学生不存在!')
    print(info)


def find_stu():
    '''查找学生信息'''
    find_name=input('请输入要查找的学生姓名:')
    global info
    for i in info:
        if find_name == i['name']:
            print(f"该学生的学号是{i['id']},该学生的电话是{i['tel']},该学生的性别是{i['sex']}")

    else:
        print('该学生不存在!')


def print_all():
    '''显示所有学员'''
    print('姓名\t性别\t电话\t学号')
    for i in info:
        print(f"{i['name']},{i['sex']},{i['tel']},{i['id']}")
while True:
   show_function()
   num = int(input("请输入要选择功能序号:"))
   if num == 1:
     add_stu()
   elif num == 2:
     del_stu()
   elif num == 3:
     change_stu()
   elif num == 4:
     find_stu()
   elif num == 5:
     print_all()
   elif num == 6:
     print(exit())
   else:
       print('输入信息有误!请重新输入!')


