import sys

#print('Hello World!')

print("你好！" , end="");


print('======= Python import sys model ======')

print('命令行参数为：')
for i in sys.argv:
    print(i)
print(' \n Python Path is ' ,sys.path)
print('----Python 中的字符串----')
str = 'this is my first py_learn string'
print(str.__sizeof__())
for i in str:
    print(i, end=" ")

