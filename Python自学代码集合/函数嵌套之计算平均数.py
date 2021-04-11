# 需求:计算三个数的和之后调用和函数来计算平均数
def sum_num(a,b,c):
    return a+b+c

def avg(a,b,c):
    sum=sum_num(a,b,c)
    print(sum/3)
avg(2,2,3)
