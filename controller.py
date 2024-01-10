from json import load
import model
import view

menu = load(open('menu_pizzeria.json', 'r', encoding='utf-8'))


@model.decorator_check
def pizzeria(value=True):
    global arr
    product_list = {}
    for i in menu:
        for product in menu[i]:
            product_list[product['number']] = [product['product'], product['price']]

    user_list = {}
    while value:
        try:
            view.display_menu(user_list)
            model.choose_product(input("Введите номер блюда!: "), user_list, product_list)
            user_list = model.delete_product(input("Желаете ли вы удалить блюдо из вашей корзины?\n1) Да 2) Нет: "), user_list)
            arr = model.pay(input("Продолжить выбор вкуснейших блюд?\n1) Да 2) Нет: "), user_list)
            value = arr[0]
        except TypeError:
            while type(arr) is not list:
                arr = model.pay(input("Продолжить выбор вкуснейших блюд?\n1) Да 2) Нет: "), user_list)

    return [arr[1], arr[2], sum(user_list), user_list]


print(f"Вас приветствует пиццерия Тимоша джонс!\nВыберите свои любимые блюда!")
pizzeria()
