# Пиццерия!
def pizzeria(value):
    prices_user = {}
    text = ""
    while value:
        if len(prices_user) == 0:
            text = "0 товаров"
        else:
            for i in prices_user:
                text += str(prices_user[i]) + " "
        print("Вас приветствует пиццерия Тимоша джонс!\nВыберите свою любимую итальянскую пиццу!\nВ вашей корзине: " + str(text))

        print("1) Пепперони, 599,99₽\n2) Сырная пицца! 549,99₽\n3) Timosha pizza! 699,99₽")
        pizza = input("Напишите номер своей любимой пиццы!: ")

        if pizza == "1":
            print("Пепперони! Отличный выбор")
            prices_user[599.99] = "Пепперони"

        elif pizza == "2":
            print("Сырная! Отличный выбор")
            prices_user[549.99] = "Сырная"

        elif pizza == "3":
            print("Timosha pizza! Прекрасный выбор!")
            prices_user[699.99] = "Timosha pizza"

        else:
            print("Этой пиццы нет в нашем ассортименте :(")

        print("Выберите соус:\n1) Без соуса(напишите без)\n2) Сырный 59,99₽\n3) Кетчуп 69,99₽\n4) Mystery sauce 99999,99₽")
        sauce = input("Введите номер соуса!: ")
        if sauce == "1":
            print("Хорошо!")
        elif sauce == "2":
            print("Соус добавлен!")
            prices_user[59.99] = "Сырный"
        elif sauce == "3":
            print("Соус добавлен!")
            prices_user[69.99] = "Кетчуп"
        elif sauce == "4":
            print("О наличии этого соуса ходят легенды, говорят, он был придуман Камоз...")
        else:
            print("Такого соуса нет в нашем ассортименте :(")
            break

        yes_or_no = input("Продолжить выбор вкуснейших пицц? (Введите Да / Нет): ")
        if yes_or_no == "Да":
            value = True
        elif yes_or_no == "Нет":
            value = False
            print("Сумма ваших товаров равна: " + str(sum(prices_user)))
            pay = input("Выберите оплату! 1) Наличные 2) Карта: ")
            if pay == "1":
                money = int(input("Положите деньги и мы вернем сдачу! "))
                if money == sum(prices_user):
                    print("Оплата закончена! Удачного дня!")
                elif money > sum(prices_user):
                    print("Ваша сдача: " + str(money - sum(prices_user)))
                    print("Оплата закончена! Удачного дня!")
                else:
                    print("Вам не хватает!")
                    break
            elif pay == "2":
                print("Приложите карту!\nОплата окончена! Удачного дня")
            else:
                print("Такого варианта оплаты нет в нашей сети пиццерий :(")
                break
        else:
            print("НАДО БЫЛО НАПИСАТЬ Да ИЛИ Нет !!!")
            break


pizzeria(True)
