#Author WenyuZheng
'''

'''

name = input("Name:")
age = int(input("Age:"))    #强制转换类型
print(type(age))            #打印变量类型
job = input("Job:")
salary = input("Salary:")

info = '''
------- info of ''' + name + '''-------
Name:''' + name + '''
Age:''' + str(age)
print(info)


info1 = '''
------- info1 of %s -------
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name,name,age,job,salary)
print(info1)




info2 = '''
------- info2 of {_name} -------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name = name,
           _age = age,
           _job = job,
           _salary = salary)

print(info2)

info3 = '''
------- info3 of {0} -------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)

print(info3)



