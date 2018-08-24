#Author WenyuZheng

'''
#文件读取
file_path = '/Users/Rex/PycharmProjects/pyexe/Day1/homework/UserInfo.txt'

with open(file_path) as file_object:
	content = file_object.read()
	print(content.rstrip())

with open(file_path) as file_object:
	for line in file_object:
		print(line.rstrip())

with open(file_path) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())


#文件写入 写入模式
file_name = 'programming.txt'

a = 3.14159
with open(file_name,'w') as file_object:
	file_object.write(str(a)+'\n')
	file_object.write(str(a))
'''

#文件写入 附加模式
file_name = 'programming.txt'

a = 'Pi = 3.14159'
with open(file_name,'a') as file_object:
	file_object.write('\n'+a+'\n')
