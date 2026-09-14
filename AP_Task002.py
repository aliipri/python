fio = input("Введите вашу фамилию, имя и отчество: ").split()

surname = fio[0]
name = fio[1]
otchestvo = fio[2]

print("Здравствуйте,", name + "!")

product1 = input("Введите первый товар: ")
product2 = input("Введите второй товар: ")
product3 = input("Введите третий товар: ")

products = [product1, product2, product3]

print()
print("Ваш список:", products)
print("Товаров в списке:", len(products))

products.append("стакан")

print()
print("Список после добавления подарка:", products)

products.sort()

print()
print("Отсортированный список:", products)

initials = name[0] + "." + otchestvo[0] + "."

print()
print("До свидания,", initials, surname + "!")