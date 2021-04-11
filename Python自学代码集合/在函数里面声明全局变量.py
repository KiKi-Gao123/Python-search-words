#定义一个全局变量在函数中声明全局变量 global
glo_num=0

def testA():
    global glo_num
    glo_num=100
    print(glo_num)

def testB():
    print(glo_num)

testA()
testB()