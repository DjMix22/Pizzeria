def choose_pizza(number, prices_user):
    if number == "1":
        print("Пепперони! Отличный выбор")
        prices_user[599.99] = "Пепперони"

    elif number == "2":
        print("Сырная! Отличный выбор")
        prices_user[549.99] = "Сырная"

    elif number == "3":
        print("Timosha pizza! Прекрасный выбор!")
        prices_user[699.99] = "Timosha pizza"

    else:
        print("Этой пиццы нет в нашем ассортименте :(")


def choose_sauce(number, prices_user):
    if number == "1":
        print("Хорошо!")
    elif number == "2":
        print("Соус добавлен!")
        prices_user[59.99] = "Сырный"
    elif number == "3":
        print("Соус добавлен!")
        prices_user[69.99] = "Кетчуп"
    elif number == "4":
        print("О наличии этого соуса ходят легенды, говорят, он был придуман Камоз...")
    else:
        print("Такого соуса нет в нашем ассортименте :(")


def pay(value, prices_user):
    if value == "1":
        return True
    elif value == "2":
        return False
        print("Сумма ваших товаров равна: " + str(sum(prices_user)))
        pay = input("Выберите оплату! 1) Наличные 2) Карта: ")
        if pay == "1":
            money = int(input("Положите деньги и мы вернем сдачу!: "))
            if money == sum(prices_user):
                print("Оплата закончена! Удачного дня!")
            elif money > sum(prices_user):
                print("Ваша сдача: " + str(money - sum(prices_user)))
                print("Оплата закончена! Удачного дня!")
            else:
                print("Вам не хватает!")
                exit()
        elif pay == "2":
            print("Приложите карту!\nОплата окончена! Удачного дня")
        else:
            print("Такого варианта оплаты нет в нашей сети пиццерий :(")
            exit()
    else:
        print("До свидания!")
        exit()


def pizzeria(value  = True):
    prices_user = {}
    while value:
        text = ""
        if len(prices_user) == 0:
            text = "0 товаров"
        else:
            for i in prices_user:
                text += str(prices_user[i]) + " "
        print("Вас приветствует пиццерия Тимоша джонс!\nВыберите свою любимую итальянскую пиццу!\nВ вашей корзине: " + str(text))

        print("1) Пепперони! 599,99₽\n2) Сырная пицца! 549,99₽\n3) Timosha pizza! 699,99₽")

        choose_pizza(input("Напишите номер своей любимой пиццы!: "), prices_user)

        print("Выберите соус:\n1) Без соуса\n2) Сырный 59,99₽\n3) Кетчуп 69,99₽\n4) Mystery sauce 99999,99₽")

        choose_sauce(input("Введите номер соуса!: "), prices_user)

        value= pay(input("Продолжить выбор вкуснейших пицц? 1) Да 2) Нет: "), prices_user)


pizzeria()


pizzeria(True)
