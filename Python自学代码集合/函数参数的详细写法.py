
#位置参数(讲究顺序)
def can_list(name,age,sex):
    print(f'我的姓名是{name},我今年{age}岁了,我是一个{sex}生')

can_list('高琪',20,'女')


#关键字参数
def can_list(name,age,sex):
    print(f'我的姓名是{name},我今年{age}岁了,我是一个{sex}生')

can_list('赵峰',age=20,sex='男')

#缺省参数
def can_list(name,sex,age=20,):
    print(f'我的姓名是{name},我今年{age}岁了,我是一个{sex}生')

can_list('高琪',sex='女')

#不定长参数
def can_list(*args):
    print(args)

can_list('高琪',12)

def can_list(**kwargs):
    print(kwargs)

can_list(name='小赵')
