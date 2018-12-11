#Author WenyuZheng
'''
#字符串处理
string1 = 'paparanoid parapa   '
print(string1.lstrip('pa'))
print(string1.rstrip('pa'))
print(string1.strip('pa'))
print(string1.lstrip())
print(string1.rstrip())
print(string1.strip())

#检查字符串中师傅存在指定字符串
if ('paparanoid  ') in string1:
	print ('y')

#替换
print(string1.replace('pa','tb'))

#字符串长度
print(len(string1))


str1 = "\"asfd \"afdad"

print(str1)
'''



print("my\tname".expandtabs(tabsize=30))

print("{i}. {name}: {price}".format_map({"i":1,"name":"jupiter","price":50}))

print("as11".isalpha())
print("as11".isdecimal())
print("as11".isdigit())
print("as11".isidentifier())
print("s11".islower())
print("as11".isnumeric())
print("as11".isprintable())
print("aaa".isidentifier())
print("+".join(["1", "2", "3"]))

rule = str.maketrans("abcdef", "@#^&*(")
print(str.translate("jupiter", rule))
print("jupiteer".replace("e", "E", 1))

print("adf\r\bad".splitlines())

