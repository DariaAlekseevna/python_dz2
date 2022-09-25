# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

num = input('введите вещественное число: ')
i = 0
j = 0
sum = 0
if float(num) > 0:

    while i < 2:
        if i == 0:
            while j < int(len(num.split('.')[i])):
                sum = sum + int(num.split('.')[i][j])
                j += 1
            i += 1
            j = 0
        if i == 1:
            while j < int(len(num.split('.')[i])):
                sum = sum + int(num.split('.')[i][j])
                j += 1
        i += 1
else:
    while i < 2:
        if i == 0:
            j = 1
            while j < int(len(num.split('.')[i])):
                sum = sum + int(num.split('.')[i][j])
                j += 1
            i += 1
            j = 0
        if i == 1:
            while j < int(len(num.split('.')[i])):
                sum = sum + int(num.split('.')[i][j])
                j += 1
        i += 1
print(f'сумма цифр в числе {num} равна {sum}')


