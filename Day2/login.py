# Author WenyuZheng


_username = 'wenyuzheng'
_password = '123456'
username = input("username:")
password = input("password:")

if _username == username and _password == password:
    print("Welcome {name} !".format(name = username))
else:
    print("Invalid username or password!")