surname = input("Введите вашу фамилию: ")
name = input("Введите ваше имя: ")

print("Добро пожаловать,", name + "! Начинаем приём заявок")

total = 0
accepted = 0

while True:
    applicant = input('\nФамилия абитуриента (или "завершить", чтобы закончить приём): ')

    if applicant == "завершить":
        break

    score = int(input("Балл абитуриента: "))
    diploma = input("Есть ли диплом олимпиады? (да/нет): ")

    total = total + 1

    if score >= 220 or (diploma == "да" and score >= 180):
        print(applicant + ": заявка одобрена")
        accepted = accepted + 1
    else:
        print(applicant + ": заявка отклонена")

print()
print("Рассмотрено абитуриентов:", total)
print("Зачислено:", accepted)

print()
print("До свидания,", name + "!")