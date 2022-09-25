#Реализуйте алгоритм перемешивания списка.
from random import random, shuffle

num = int(input('введите количество элементов в списке: '))
num_list = []
for i in range(num):
    num_list.append(input("введите элемент в списке: "))

print("список заданный пользователем: ", num_list)

shuffle(num_list)
print('перемешанный список: ', num_list)


