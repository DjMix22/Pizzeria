import json

menu = json.load(open('menu.json', 'r', encoding="utf-8"))


def decorator_check(pizzeria):
    def wrapper():
        lst = pizzeria()
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


def choose_product(number, prices_user):
    if number == "1":
        print("Пепперони! Отличный выбор")
        prices_user[599.99] = "Пепперони"

    elif number == "2":
        print("Сырная! Отличный выбор")
        prices_user[549.99] = "Сырная пицца"

    elif number == "3":
        print("Timosha pizza! Прекрасный выбор!")
        prices_user[699.99] = "Timosha pizza"

    elif number == "4":
        print("Соус добавлен!")
        prices_user[59.99] = "Сырный соус"

    elif number == "5":
        print("Соус добавлен!")
        prices_user[69.99] = "Кетчуп"

    elif number == "6":
        print("О наличии этого соуса ходят легенды...")
        prices_user[99999.99] = "Mystery sauce"

    else:
        print("Этого блюда нет в нашем ассортименте :(")


def pay(value, prices_user):
    if value == "1":
        value_new = True
    elif value == "2":
        value_new = False

        print(f"Сумма ваших товаров равна: {sum(prices_user)}")

        global pay
        pay = input("Выберите оплату! 1) Наличные 2) Карта: ")

        global money
        if pay == "1":
            money = int(input("Положите деньги и мы вернем сдачу!: "))
            if money == sum(prices_user):
                print("Оплата закончена!  Удачного дня!")
            elif money > sum(prices_user):
                print(f"Ваша сдача: {money - sum(prices_user)}")
                print("Оплата закончена! Удачного дня!")
            else:
                print("Вам не хватает!")
                exit()
        elif pay == "2":
            money = sum(prices_user)
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
    prices_user = {}
    while value:
        text = ""
        if len(prices_user) == 0:
            text = "0 товаров"
        else:
            for i in prices_user:
                text += str(prices_user[i]) + " "
        print(f"Вас приветствует пиццерия Тимоша джонс!\nВыберите свои любимые блюда!\nВ вашей корзине: {text}")
        print("Пиццы:\n1) Пепперони! 599,99₽\n2) Сырная пицца! 549,99₽\n3) Timosha pizza! 699,99₽\nСоусы:\n4) Сырный! "
              "59,99₽\n5) Кетчуп! 69,99₽\n6) Mystery sauce! 99999,99₽")

        choose_product(input("Введите номер блюда!: "), prices_user)

        value = pay(input("Продолжить выбор вкуснейших пицц? 1) Да 2) Нет: "), prices_user)

    return [pay, money, sum(prices_user), prices_user]


pizzeria()
