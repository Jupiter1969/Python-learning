# Author WenyuZheng

#浅copy举例：联合账户
'''
person = ["name",["saving",0]]

hus = person[:]
wif = person[:]

hus[0] = "Rex"
wif[0] = "Joy"

hus[1][1] = 50

print(hus)
print(wif)
'''

names = ("Rex","Joy")
print(names)

