from json import load

menu = load(open('menu_pizzeria.json', 'r', encoding='utf-8'))


def delete_product(number, user_list):
    if number != "1" and number != "2":
        print("Не верное значение")
        delete_product(input("Желаете ли вы удалить блюдо из вашей корзины?\n1) Да 2) Нет: "), user_list)
    else:
        if number == "1":
            for i in user_list:
                print(user_list[i])
            product = input("Введите название товара: ")
            user_list = {j : i for i, j in user_list.items()}
            print(f"Товар {product} успешно удален!")
            del user_list[product]
            user_list = {j: i for i, j in user_list.items()}
            return user_list
        else:
            return user_list


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


def choose_product(number, user_list):
    product_list = {}
    for i in menu:
        for product in menu[i]:
            product_list[product['number']] = [product['product'], product['price']]

    if number in product_list:
        print(f"{product_list[number][0]}! Отличный выбор!")
        user_list[product_list[number][1]] = product_list[number][0]
    else:
        print("Такой товар не найден")
        choose_product(input("Введите номер блюда!: "), user_list)


def pay(value, user_list):
    if value == "1":
        value_new = True
    elif value == "2":
        value_new = False

        print(f"Сумма ваших товаров равна: {sum(user_list)}")

        global pay
        pay = input("Выберите оплату! 1) Наличные 2) Карта: ")

        global money
        if pay == "1":
            money = int(input("Положите деньги и мы вернем сдачу!: "))
            if money == sum(user_list):
                print("Оплата закончена!  Удачного дня!")
            elif money > sum(user_list):
                print(f"Ваша сдача: {money - sum(user_list)}")
                print("Оплата закончена! Удачного дня!")
            else:
                print("Вам не хватает!")
                exit()
        elif pay == "2":
            money = sum(user_list)
            print("Приложите карту!\nОплата окончена! Удачного дня")
        else:
            print("Такого варианта оплаты нет в нашей сети пиццерий :(")
            exit()
    else:
        print("До свидания!")
        exit()
    return value_new


@decorator_check
def pizzeria():
    value = True
    user_list = {}
    while value:
        text = ""
        if len(user_list) == 0:
            text = "0 товаров"
        else:
            for i in user_list:
                text += str(user_list[i]) + " "
        print(f"Вас приветствует пиццерия Тимоша джонс!\nВыберите свои любимые блюда!\nВ вашей корзине: {text}")
        print("Пиццы:\n1) Пепперони! 599,99₽\n2) Сырная пицца! 549,99₽\n3) Timosha pizza! 699,99₽\nСоусы:\n4) Сырный! "
              "59,99₽\n5) Кетчуп! 69,99₽\n6) Mystery sauce! 99999,99₽")

        choose_product(input("Введите номер блюда!: "), user_list)

        user_list = delete_product(input("Желаете ли вы удалить блюдо из вашей корзины?\n1) Да 2) Нет: "), user_list)
        value = pay(input("Продолжить выбор вкуснейших блюд?\n1) Да 2) Нет: "), user_list)

    return [pay, money, sum(user_list), user_list]


pizzeria()
