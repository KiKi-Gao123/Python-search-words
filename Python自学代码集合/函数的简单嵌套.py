#需求:在A函数中调用嵌套B函数


def testB():
    print('B函数开始执行!')
    print('B函数执行的代码!')
    print('B函数结束执行!')

def testA():
    print('A函数开始执行!')
    testB()
    print('A函数结束执行!')

testA()