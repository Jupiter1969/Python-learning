# Author WenyuZheng
'''
实现行政区划三级菜单
1. 每级菜单进入后显示所有选项
2. 输入某个选项进入下一级菜单
   输错提示输错，重新输入
   输入Q退出程序
   输入B返回上一层
'''

import json

file_path = '/Users/Rex/PycharmProjects/pyexe/Day1/admin_divisions.json'
admin_div = {}
prov_list = []
with open (file_path) as f_obj:
    admin_div = json.load(f_obj)

num_pro = len(admin_div) #省个数
prov_list = list(admin_div.keys()) #省列表

while 1:
    # 输出省列表
    print("**********行政区划***********")
    for i in range(num_pro):
        print(prov_list[i])
    prov = input("输入你想查看的省(退出程序请输入Q+Enter)：")
    if(prov == "Q"):
        exit(0)
    else:
        try:
            city_list = list(admin_div[prov])
        except KeyError:
            print("你输入的省不存在.")
            continue
        else:
            while 1:
                #输出市列表
                print('**********行政区划-{p}***********'.format(p = prov))
                num_city = len(city_list)
                for i in range(num_city):
                    print(city_list[i])
                city = input("输入你想查看的市(退出程序请输入Q+Enter.返回上一层请输入B+Enter.)：")
                if (city == "Q"):
                    exit(0)
                elif(city == 'B'):
                    break
                else:
                    try:
                        county_list = admin_div[prov][city]
                    except KeyError:
                        print("你输入的市不存在.")
                        continue
                    else:
                        #输出县列表
                        print('**********行政区划-{c}***********'.format(c=city))
                        num_county = len(county_list)
                        for i in range(num_county):
                            print(county_list[i])
                        while 1:
                            nextstep = input("退出请输入Q+Enter.返回上一层请输入B+Enter.")
                            if (nextstep == 'B'):
                                break
                            elif (nextstep == 'Q'):
                                exit(0)
                            else:
                                continue






