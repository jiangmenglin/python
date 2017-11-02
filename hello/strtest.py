a = 'hello'
b = 'world'

print(" a + b 输出结果：", a + b)
print(" a * 2 输出结果是 ：", a * 2)
print(" a[1]的值是：", a[1])
print(" a[0:4]输出是：", a[0:4])


def containsH(h, str):
    if 'h' in a:
        print('%s中含有%s'%(str, h))
    else:
        print('%s中不含有%s'%(str, h))
print(containsH('f', a))
print(containsH('w', b))

print("字符串%s的长度是%d" % (b, len(b)))
for i in range(0,len(b), 2):
    print(b[i], end=" ")
