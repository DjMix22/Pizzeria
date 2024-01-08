def decorator_check(func):
    def wrapper():
        lst = func()
        print("\n" + '*' * 32)
        print("*{: ^30}*".format("*** Чек ***"))
        print("*{: ^30}*".format("Список товаров:"))
        for product in lst[3]:
            print("*{: ^30}*".format(lst[3][product]))
        print("*{: ^30}*".format("Цена товара:"))
        print("*{: ^30.2f}*".format(lst[2]))
        print("*{: ^30}*".format("Вид оплаты:"))
        print("*{: ^30}*".format({"1": "Наличные", "2": "Карта"}[lst[0]]))
        print("*{: ^30}*".format("Сумма оплаты:"))
        print("*{: ^30.2f}*".format(lst[1]))
        if lst[0] == "1":
            print("*{: ^30}*".format("Сдача:"))
            print("*{: ^30.2f}*".format(lst[1] - lst[2]))
        print('*' * 32)

    return wrapper


def choose_product(number, user_list, product_list):
    if number in product_list:
        print(f"{product_list[number][0]}! Отличный выбор!")
        user_list[product_list[number][1]] = product_list[number][0]
    else:
        print("Такой товар не найден")
        choose_product(input("Введите номер блюда!: "), user_list)


def delete_product(number, user_list, j=0):
    products = {}
    for i in user_list:
        j += 1
        products[str(j)] = user_list[i]
    if number != "1" and number != "2":
        print("Неверное значение")
        delete_product(input("Желаете ли вы удалить блюдо из вашей корзины?\n1) Да 2) Нет: "), user_list)
    else:
        if number == "1":
            print("Товары:")
            for i in range(len(products)):
                print(f"{i + 1}) {products[str(i + 1)]}")
            product = input("Введите номер товара: ")
            if product in products:
                user_list = {j: i for i, j in user_list.items()}
                print(f"Товар {products[product]} успешно удален!")
                del user_list[products[product]]
                user_list = {j: i for i, j in user_list.items()}
            return user_list
        else:
            return user_list


def pay(value, user_list):
    if value == "1":
        value_new = True
        return [value_new]
    elif value == "2":
        value_new = False

        print(f"Сумма ваших товаров равна: {sum(user_list)}")

        payment = input("Выберите оплату! 1) Наличные 2) Карта: ")

        if payment == "1":
            money = int(input("Положите деньги и мы вернем сдачу!: "))
            if money == sum(user_list):
                print("Оплата закончена!  Удачного дня!")
                return [value_new, payment, money]
            elif money > sum(user_list):
                print(f"Ваша сдача: {money - sum(user_list)}")
                print("Оплата закончена! Удачного дня!")
                return [value_new, payment, money]
            else:
                print("Вам не хватает!")
                exit()
        elif payment == "2":
            money = sum(user_list)
            print("Приложите карту!\nОплата окончена! Удачного дня")
            return [value_new, payment, money]
        else:
            print("Неверное значение!")
            pay(input("Продолжить выбор вкуснейших блюд?\n1) Да 2) Нет: "), user_list)

    else:
        print("Неверное значение!")
        pay(input("Продолжить выбор вкуснейших блюд?\n1) Да 2) Нет: "), user_list)
