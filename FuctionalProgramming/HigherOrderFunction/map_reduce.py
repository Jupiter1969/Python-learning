# Author WenyuZheng
from functools import reduce

# map()
# 传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

def power(x=0):
    return x * x


print(list(map(power, [1, 2, 3, 4, 5])))

# reduce()
# 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def int(x, y):
    return x * 10 + y

print(reduce(int, [1,2,3,4,5]))

Digits = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
          }

#字符串转整数


def str2int(str):

    def digit(s):
        return Digits[s]

    def cal(x, y):
        return x * 10 + y
    return reduce(cal, list(map(digit, str)))
print(str2int('4352'))

# 使用lambda进一步简化
'''
Lambda表达式是Python中一类特殊的定义函数的形式，使用它可以定义一个匿名函数。
与其它语言不同，Python的Lambda表达式的函数体只能有单独的一条语句，也就是返回值表达式语句
'''
def str2int(str):

    def digit(s):
        return Digits[s]

    return reduce(lambda x, y: x*10 + y, list(map(digit, str)))

print(str2int('4352'))


