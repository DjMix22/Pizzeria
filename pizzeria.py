def my_decorator(pizzeria):
    def wrapper():
        arr = pizzeria()
        print("-----Чек-----")
        print(arr[0])
        print(arr[1])
        print(arr[2])
        print("-----Спасибо за покупку-----")
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
        print("Хорошо!")

    elif number == "5":
        print("Соус добавлен!")
        prices_user[59.99] = "Сырный соус"

    elif number == "6":
        print("Соус добавлен!")
        prices_user[69.99] = "Кетчуп"

    elif number == "7":
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


@my_decorator
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
        print("Пиццы:\n1) Пепперони! 599,99₽\n2) Сырная пицца! 549,99₽\n3) Timosha pizza! 699,99₽\nСоусы:\n4) Без "
              "соуса\n5) Сырный! 59,99₽\n6) Кетчуп! 69,99₽\n7) Mystery sauce! 99999,99₽")

        choose_product(input("Введите номер блюда!: "), prices_user)

        value = pay(input("Продолжить выбор вкуснейших пицц? 1) Да 2) Нет: "), prices_user)

        return [pay, money, sum(prices_user)]

pizzeria()
