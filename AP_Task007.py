def load_catalog(filename):
    catalog = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(";")

                if len(parts) != 4:
                    print("Ошибка в строке:", line)
                    continue

                try:
                    book_id = int(parts[0])
                    name = parts[1]
                    price = int(parts[2])
                    quantity = int(parts[3])

                    if price <= 0:
                        print("Цена должна быть больше 0. Строка пропущена.")
                        continue

                    if quantity < 0:
                        print("Количество не может быть меньше 0. Строка пропущена.")
                        continue

                    catalog[book_id] = (name, price, quantity)

                except ValueError:
                    print("Ошибка в строке:", line)
                    print("ID, цена и количество должны быть целыми числами.")

        print("Файл", filename, "загружен. Книг в каталоге:", len(catalog))

    except FileNotFoundError:
        print("Файл", filename, "не найден.")

    return catalog


def save_catalog(filename, catalog):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for book_id in sorted(catalog):
                name, price, quantity = catalog[book_id]

                file.write(
                    str(book_id) + ";" +
                    name + ";" +
                    str(price) + ";" +
                    str(quantity) + "\n"
                )

        print("Каталог сохранён в файл", filename + ".")

    except OSError:
        print("Не удалось сохранить файл.")


def print_catalog(catalog):
    if len(catalog) == 0:
        print("Каталог пуст.")
        return

    print()
    print("Каталог:")

    for book_id in sorted(catalog):
        name, price, quantity = catalog[book_id]

        if quantity == 0:
            print(book_id, ".", name, "—", price, "руб., нет в наличии")
        else:
            print(book_id, ".", name, "—", price, "руб., остаток:", quantity)


def add_book(catalog):
    try:
        book_id = int(input("ID новой книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id in catalog:
        print("Книга с таким ID уже есть.")
        return False

    name = input("Название: ")

    try:
        price = int(input("Цена: "))
    except ValueError:
        print("Цена должна быть целым числом.")
        return False

    if price <= 0:
        print("Цена должна быть больше 0.")
        return False

    try:
        quantity = int(input("Количество: "))
    except ValueError:
        print("Количество должно быть целым числом.")
        return False

    if quantity < 0:
        print("Количество не может быть меньше 0.")
        return False

    catalog[book_id] = (name, price, quantity)

    print("Книга «" + name + "» добавлена.")

    return True


def delete_book(catalog):
    try:
        book_id = int(input("ID книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id not in catalog:
        print("Книги с таким ID нет.")
        return False

    name = catalog[book_id][0]

    del catalog[book_id]

    print("Книга «" + name + "» удалена.")

    return True


def change_price(catalog):
    try:
        book_id = int(input("ID книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id not in catalog:
        print("Книги с таким ID нет.")
        return False

    try:
        new_price = int(input("Новая цена: "))
    except ValueError:
        print("Цена должна быть целым числом.")
        return False

    if new_price <= 0:
        print("Цена должна быть больше 0.")
        return False

    name, price, quantity = catalog[book_id]

    catalog[book_id] = (name, new_price, quantity)

    print("Цена книги «" + name + "» изменена на", new_price, "руб.")

    return True


def change_quantity(catalog):
    try:
        book_id = int(input("ID книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id not in catalog:
        print("Книги с таким ID нет.")
        return False

    try:
        new_quantity = int(input("Новое количество: "))
    except ValueError:
        print("Количество должно быть целым числом.")
        return False

    if new_quantity < 0:
        print("Количество не может быть меньше 0.")
        return False

    name, price, quantity = catalog[book_id]

    catalog[book_id] = (name, price, new_quantity)

    print("Количество книги «" + name + "» изменено на", new_quantity)

    return True


filename = "catalog.txt"

catalog = load_catalog(filename)

while True:
    print()
    print("Меню:")
    print("1 — показать каталог")
    print("2 — добавить книгу")
    print("3 — удалить книгу")
    print("4 — изменить цену")
    print("5 — изменить количество")
    print("0 — сохранить и выйти")

    try:
        choice = int(input("Выберите пункт: "))
    except ValueError:
        print("Введите номер пункта меню.")
        continue

    if choice == 1:
        print_catalog(catalog)

    elif choice == 2:
        add_book(catalog)

    elif choice == 3:
        delete_book(catalog)

    elif choice == 4:
        change_price(catalog)

    elif choice == 5:
        change_quantity(catalog)

    elif choice == 0:
        save_catalog(filename, catalog)
        print("До свидания!")
        break

    else:
        print("Такого пункта меню нет.")