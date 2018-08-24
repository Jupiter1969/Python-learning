#Author WenyuZheng
'''
-------Program Summary-------
Simple logon function
1. 3 chances to try each time you run the program
2. User account will be locked after 3 wrong shots, and times of wrong shots will be recorded even if you restart the program.
'''

import json
file_path = '/Users/Rex/PycharmProjects/pyexe/Day1/UserInfo.json'

user_info = {}

with open (file_path) as f_obj:
	user_info = json.load(f_obj)

for i in range (3):
    username = input('Username:')
    password = input('Password:')
    try:
        postion = user_info['Username'].index(username)
    except ValueError:
        if(i < 2):
            print('Wrong username or password!\n' + str(2 - i) + ' times left.')
        else:
            break
        continue
    else:
        if(user_info['Lock status'][postion] == 3):
            print('User ' + username + ' has been locked.')
            break
        if password == user_info['Password'][postion]:
            print('Welcome {name}!'.format(name = username))
            user_info['Lock status'][postion] = 0
            json_obj = json.dumps(user_info)
            with open(file_path, 'w') as f_obj:
                f_obj.write(json_obj)
            break
        elif (i<2):
            print('Wrong username or password!\n' + str(2 - i) + ' times left.')
            user_info['Lock status'][postion] += 1
        else:
            user_info['Lock status'][postion] = 1
            print('Wrong username or password!\n')
        json_obj = json.dumps(user_info)
        with open(file_path, 'w') as f_obj:
            f_obj.write(json_obj)