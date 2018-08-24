# Author WenyuZheng

import sys

#print(sys.path) #打印环境变量
#print(sys.argv) #当前脚本相对路径
#print(sys.argv[0])


import os

cmd_result = os.system("df")  #//(相当于windows  dir)只执行命令，不保存结果
cmd_result = os.popen("df")   #执行df命令，返回执行结果的内存地址
cmd_result = os.popen("df").read() #读取内存地址，才是df执行的结果
print(cmd_result)  #os.system --> cmd_result是处理是否成功的结果，不是命令执行的结果

#在当前目录下创建新目录
#os.mkdir("new_dir")



