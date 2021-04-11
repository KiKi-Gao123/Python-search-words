#1.定义函数 2.调用函数

def sum_num(a,b):
    '''
    求和函数
    :param a: 参数1
    :param b: 参数2
    :return: 结果
    '''
    return a+b

sum = sum_num(123,234)
print(sum)


help(sum_num(1,2))