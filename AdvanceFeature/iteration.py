# Author WenyuZheng
from collections import Iterable
from collections import Iterator

'''
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
'''

#判断是否是可迭代对象Iterable/迭代器Iterator
print(isinstance(222, Iterable))
print(isinstance(222, Iterator))
print(isinstance('jupiter', Iterable))
print(isinstance('jupiter', Iterator))
print(isinstance([1,2,3], Iterable))
print(isinstance([1,2,3], Iterator))
print(isinstance(iter([1,2,3]), Iterator))
print(isinstance({'name':'Jupiter', 'age':'30'}, Iterable))

#实现下标循环
for i, value in enumerate('abc'):
    print(i, value)

for x, y in [(1,3),(2,3),(4,4)]:
    print(x , ': ', y)

#dict的items()可以同时迭代key和value
people = {'name': 'Jupiter', 'age': '30', 'sex': 'female'}
for key, value in people.items():
    print(key, ':', value)

#请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L = None):
    if L == None or len(L) == 0:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if i < min:
                min = i
            if i > max:
                max = i
        return(min, max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')