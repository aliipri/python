prices = {
    "хлеб": 50,
    "молоко": 90,
    "сыр": 400,
    "яблоки": 120,
    "кофе": 350
}


def print_menu(prices):
    print("Товары в продаже:")

    for product in prices:
        print(product, "—", prices[product], "руб.")


def ask_quantity(product):
    quantity = int(input("Сколько «" + product + "»? "))
    return quantity


def item_cost(price, quantity):
    cost = price * quantity
    return cost


def print_receipt(cart):
    print()
    print("--- Чек ---")

    total = 0

    for i in range(len(cart)):
        product, quantity, cost = cart[i]

        print(i + 1, ".", product, "×", quantity, "=", cost, "руб.")

        total = total + cost

    print("Сумма:", total, "руб.")

    return total


def apply_discount(total, card=False):
    if card == True:
        discount = int(total * 0.10)
    elif total >= 1000:
        discount = int(total * 0.05)
    else:
        discount = 0

    pay = total - discount

    return discount, pay


name = input("Введите имя кассира: ")

print("Здравствуйте,", name + "! Касса открыта")

print_menu(prices)

cart = []

while True:
    print()

    product = input('Товар (или "оплата", чтобы перейти к оплате): ')

    product = product.strip().lower()

    if product == "оплата":
        break

    if product not in prices:
        print("Товара «" + product + "» нет в продаже")
        continue

    quantity = ask_quantity(product)

    price = prices[product]

    cost = item_cost(price, quantity)

    cart.append((product, quantity, cost))

    print("Добавлено:", product, "×", quantity, "=", cost, "руб.")

print()

card_answer = input("Есть карта магазина? (да/нет): ")

card_answer = card_answer.strip().lower()

if card_answer == "да":
    card = True
else:
    card = False

total = print_receipt(cart)

discount, pay = apply_discount(total, card=card)

different = set()

for item in cart:
    different.add(item[0])

print("Скидка:", discount, "руб.")
print("К оплате:", pay, "руб.")
print("Разных товаров в чеке:", len(different))

print()
print("Спасибо за работу,", name + "!")