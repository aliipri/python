fam = input("Введите вашу фамилию: ")
imya = input("Введите ваше имя: ")

print("Добро пожаловать,", imya + "! Начинаем принимать зачёт")

kol_sport = int(input("Сколько спортсменов сдают зачёт: "))
kol_pod = int(input("Сколько подходов делает каждый: "))

familii = []
summi = []

norma = 0

for i in range(kol_sport):
    print()
    print("--- Спортсмен", i + 1, "---")

    fam_sport = input("Фамилия спортсмена: ")
    vsego = 0

    for j in range(kol_pod):
        pod = int(input("Подход " + str(j + 1) + ": "))
        vsego = vsego + pod

    familii.append(fam_sport)
    summi.append(vsego)

    if vsego >= 30:
        print(fam_sport + ": всего", vsego, "— норматив выполнен")
        norma = norma + 1
    else:
        print(fam_sport + ": всего", vsego, "— норматив не выполнен")

print()
print("Итоговая таблица:")

for i in range(len(familii)):
    print(i + 1, ".", familii[i], "—", summi[i])

print()
print("Норматив выполнили:", norma, "из", kol_sport)
print("Всего подтягиваний группы:", sum(summi))

print()
print("До свидания,", imya + "!")