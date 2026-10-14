imya_org = input("Введите ваше имя: ")

print("Здравствуйте,", imya_org + "! Открываем зрительское голосование")

filmy = ["дюна", "аватар", "матрица", "интерстеллар", "шрек"]

print("Фильмы в программе фестиваля:", ", ".join(filmy))

progolosovali = set()

golosa = {
    "дюна": 0,
    "аватар": 0,
    "матрица": 0,
    "интерстеллар": 0,
    "шрек": 0
}

vse_filmy = set(filmy)
vybrali = set()
obshie = set(filmy)

kol_zriteley = 0

while True:
    print()

    imya = input('Имя зрителя (или "стоп", чтобы закончить): ')

    imya_proverka = imya.strip().lower()

    if imya_proverka == "стоп":
        break

    if imya_proverka in progolosovali:
        print(imya + ", вы уже голосовали, второй голос не засчитан")
        continue

    progolosovali.add(imya_proverka)
    kol_zriteley = kol_zriteley + 1

    stroka = input("Какие фильмы вам понравились (через запятую): ")

    spisok = stroka.split(",")

    vibor = set()

    for film in spisok:
        film = film.strip().lower()

        if film in vse_filmy:
            vibor.add(film)
        else:
            print("Фильма «" + film + "» нет в программе, голос не засчитан")

    for film in vibor:
        golosa[film] = golosa[film] + 1

    vybrali = vybrali | vibor
    obshie = obshie & vibor

    print("Спасибо,", imya + "! Засчитано голосов:", len(vibor))

print()
print("Итоги голосования")
print("Проголосовало зрителей:", kol_zriteley)

for film in filmy:
    print(film, "-", golosa[film])

pobeditel = filmy[0]

for film in filmy:
    if golosa[film] > golosa[pobeditel]:
        pobeditel = film

print("Победитель:", pobeditel, "(" + str(golosa[pobeditel]) + ")")

if kol_zriteley > 0 and len(obshie) > 0:
    print("Понравились всем:", end=" ")

    for film in filmy:
        if film in obshie:
            print(film, end=" ")

    print()
else:
    print("Фильмов, которые понравились всем, нет")

nikto = vse_filmy - vybrali

if len(nikto) > 0:
    print("Не выбрал никто:", end=" ")

    for film in filmy:
        if film in nikto:
            print(film, end=" ")

    print()
else:
    print("Нет фильмов, за которые никто не проголосовал")

print()
print("До свидания,", imya_org + "!")