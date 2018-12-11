# Author WenyuZheng
'''
#list切片
numbers = list(range(100))
print(numbers)

print(numbers[0:10])
print(numbers[:10])
print(numbers[-3:])
print(numbers[-3:-1])

#前十个数字，每两个取一个
print(numbers[0:10:2])
#每十个取一个
print(numbers[::10])

#tuple,字符串也可以切片，切片结果数据类型保持不变
numbers1 = tuple(range(10))
print(numbers1)
print(numbers1[0:10])
str = 'Jupiter'
print(str[2:3])
'''

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(str = ''):
    if len(str) == 0:
        return ''
    left = 0
    right = len(str) - 1
    while str[left] == ' ' and left < right:
        left = left + 1
    while str[right] == ' ' and right > left:
        right = right - 1
    if left == right:
        return ''
    else:
        return str[left:right+1]

#递归实现
def trim_recurstion(s = ''):
    if s == '':
        return ''
    elif s[0] == ' ':
        return trim_recurstion(s[1:len(s)])
    elif s[len(s)-1] == ' ':
        return trim_recurstion(s[0:len(s)-2])
    else:
        return s





# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')

# 测试:
if trim_recurstion('hello  ') != 'hello':
    print('测试失败1!')
elif trim_recurstion('  hello') != 'hello':
    print('测试失败2!')
elif trim_recurstion('  hello  ') != 'hello':
    print('测试失败3!')
elif trim_recurstion('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim_recurstion('') != '':
    print('测试失败5!')
elif trim_recurstion('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')