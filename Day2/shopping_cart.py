# Author WenyuZheng
# \033[显示方式;字体色;背景色m ...... [\ 033 [0m]
# 工资
salary = 0
# 商品列表
product_list = [
    ("Mug", 30),
    ("Refrigerator", 6500),
    ("Nintendo Switch", 2100),
    ("Giant Aimez SL 1", 4700),
    ("Mac Pro", 18000),
    ("T-shirt", 200),
    ("The Crowd: A Study of the Popular Mind", 15)
]

# 购物车
cart = []

def shopping_cart():
    while True:
        try:
            salary = input("\033[1;32m Input salary: \033[0m")

            if salary == "exit":
                print("\033[1;31m Bye~ \033[0m")
                return
            elif int(salary) == 0:
                print("\033[1;31m No Balance! Bye~ \033[0m")
                return
            else:
                break
        except ValueError:
            print("\033[1;31m Invalid input!\033[0m")
            continue
    while True:
        try:
            # 输出商品列表
            print("\033[1;34m Balance: [%s] \033[0m" % salary)
            print("\033[1;36m---------Product List:---------\033[0m")
            for index, value in enumerate(product_list):
                print("{i}. {name}: {price}".format(i=index + 1, name=value[0], price=value[1]))

            number = input("\033[1;32m Input number of the product you want: \033[0m")
            if number == 'exit' or int(salary) == 0:
                if len(cart) > 0:
                    print("\033[1;34m Balance: [%s] \033[0m" % salary)
                    print("\033[1;34m Product purchased: \033[0m")
                    for index, value in enumerate(cart):
                        print("{i}. {name}: {price}".format(i=index + 1, name=value[0], price=value[1]))
                    return
                else:
                    print("\033[1;32m Nothing purchased. \033[0m")
                    return
            elif int(number) < 1 or int(1) > len(product_list):
                print("\033[1;31m Invalid number!\033[0m")
                continue
            else:
                if product_list[int(number)-1][1] > int(salary):
                    print("\033[1;31m Insufficient balance!\033[0m")
                else:
                    cart.append(product_list[int(number)-1])
                    salary = int(salary) - product_list[int(number)-1][1]
        except ValueError:
            print("\033[1;31m Invalid input!\033[0m")
            continue


shopping_cart()


