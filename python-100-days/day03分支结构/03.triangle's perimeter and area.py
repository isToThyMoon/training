"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

"""
x = input('dada')
print(type(x))
a = float(input('边a为：'))
b = float(input('边b为：'))
c = float(input('边c为：'))

if a + b > c and a + c > b and b + c > a:
    print('a b c构成三角形周长为：%.2f' % (a+b+c))
    p = (a+b+c) / 2
    area = (p * (p-a) * (p-b) * (p-c))** 0.5
    print('a b c构成三角形面积为：%.2f' % area)

else:
    print('a b c不能构成三角形')
