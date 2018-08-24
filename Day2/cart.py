# Author WenyuZheng

cart

while(1):
    try:
        salary = int(input("Input salary:"))
    except ValueError:
        print("Invalid input!")
    else:
        break

print(salary)


