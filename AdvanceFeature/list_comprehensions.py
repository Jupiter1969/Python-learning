# Author WenyuZheng

#列表生成器
print(list(range(2, 5)))

str_list = [x + y for x in 'XYZ' for y in 'LMN']
num_list = [x * y for x in range(1, 4) for y in range(1, 4)]
num_list2 = [x * x for x in range(10) if x % 2 == 0]

print(str_list)
print(num_list)
print(num_list2)


people = {'name': 'Jupiter', 'age': '30', 'sex': 'female'}
people1 = [k.upper() + '=' + v for k, v in people.items()]
print(people1)

