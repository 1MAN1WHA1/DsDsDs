cash = {1: 10, 5: 5, 7: 4, 10: 2, 15: 3}
products = {"молоко": 20, "хлеб": 17, "йогурт": 25, "пармезан": 30, "подушечеки": 40, "кофе": 45, "чай": 10, "сок": 35,
            "вода": 50, "масло": 50}
invent = {}
money = [1, 5, 7, 10, 15]


def returnChange(change, cash):
    toGiveBack = {}
    for pos, coin in enumerate(reversed(cash)):
        while coin <= change and cash[coin] > 0:
            change = change - coin
            toGiveBack[coin] = toGiveBack.get(coin, 0) + 1
            cash[coin] -= 1
    return toGiveBack


while True:
    print(f'Продукты, которые есть в магазине: {products}')
    print('1. Добавить в корзину продукт')
    print('2. Перенести назад на полку магазина')
    print('3. Оплатить заказ')
    choice = input('Что вы хотите сделать: ')

    if choice == 'добавить':
        aditem = input('Что вы хотите положить в корзину: ')
        if aditem in products:
            invent[aditem] = products[aditem]
            del products[aditem]
            print(f'Корзина: {invent}')
        else:
            print("Данного продукта нет в магазине.")

    elif choice == 'перенести':
        oditem = input('Что вы хотите перенести назад на полку: ')
        if oditem in invent:
            products[oditem] = invent[oditem]
            del invent[oditem]
            print(f'Корзина: {invent}')
        else:
            print("Данного продукта нет в вашей корзине.")

    elif choice == 'оплатить':
        print(f'Можно оплатить вот этими купюрами {money}')
        money_one = int(input('Какими монетами вы хотите оплатить: '))
        if money_one in money:
            money_two = int(input('Сколько монет вы дадите: '))
            cash[money_one] += money_two
            sale = money_two * money_one
            total_price = sum(invent.values())
            print(f'Всего вы дали {sale} рублей.')

            if sale >= total_price:
                change = sale - total_price
                print(f'Ваша сдача: {change}')
                coins_change = returnChange(change, cash)
                print(f'Монеты в сдаче: {coins_change}')

                for coin, count in coins_change.items():
                    cash[coin] -= count
                print(f'Теперь в кассе: {cash}')
            else:
                print("Недостаточно денег для оплаты.")
        else:
            print("Введите правильный номинал монеты.")

    else:
        print('Введите правильное действие из списка')