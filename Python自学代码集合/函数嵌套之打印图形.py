#需求:打印五行直线

def print_line():
    print('----'*5)

def print_lines(num):
    i=0
    while i<num:
        print_line()
        i=i+1

print_lines(10)