from json import load

menu = load(open('menu_pizzeria.json', 'r', encoding='utf-8'))


def display_menu(user_list):
    text = ""
    if len(user_list) == 0:
        text = "0 товаров"
    else:
        for i in user_list:
            text += str(user_list[i]) + " "
    print(f"В вашей корзине: {text}")

    for i in menu:
        print(f"{i}:")
        for product in menu[i]:
            print(f"{product['number']}) {product['product']}! {product['price']}₽")
