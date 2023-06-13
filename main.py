#int
numbe =5

#Flaat
pricce =100.5

#str
name="abraham"

#bool
status= True
'''коментарии'''

print('Привет. '+name+'!')
print("сумма на $"+str(pricce))

print("Код доступа \"123\" ")# Экран
print("Привет,\n МИР!")
weather1 = "Облачнно"
sum =100.5
 # Привет Abraham сейчас на улице облвчно, а у тебя в кормане ...$!
print("Привет, "+name+"!" )
print("Сейчас на улице "+weather1+", а у тебя в кармане "+str(sum)+"$")

print(F" ПРивет, {name}!")
print(f"сейчас на улице {weather1}, а у тебя в кармане {sum}$")
weight = input("Введите ваш вес: ")# запрашиваем вес человека

print(f"Ваш вес: {weight}КГ")

# модули, плагины в прогамме

import random

print( random.randint(1, 5) )

# матемотические операции +, -, *, /, //(делить без остатка),**(возведение в степень),%(денелине по модулю), унарный минус, округление. Пи

a=10
b=5
c=4.6
print(a+b)
print(a//b)
print(a**4)# возвод в 4 степень
print(a % b)# деленая по модулю
print(-a)
print(--a)# унарный минус
print( round(c) )

import math

print( math.floor(c))# Округление а меньшую сторону
print(  math.ceil(c)  ) # Округления в большую сторону
print(math.pi)
# написание программы угадай число

import random
random_namber= random.randint(1, 5)
User_number= input("Угадай число: от 1 до 5  ")

if User_number == random_namber: #Равенство
    print("Вы угадали! ")
    print(123)
else:
    print("ВЫ не угадали :(")
    print(f"Было загадоно число {random_namber}")
age = input("Введите свой возрост: ")

if int(age) >= 18 and int( age) < 30 :
    print("доступ разрешон")
else:
    print("доступ запрещен ")
    print("Завершение программы ...")
#Дополнительныее модули из интернета
from colorama import init
print("11")
init()

# Калькулятор
a=float(input("Ведите первое число "))
b=float(input("Ведите Второе число "))

operation = input("Что сделать? (+, -): ")
result = 0
if operation == "+":
    result = a+b
elif operation == "-": #Дополнительное условия
    result= a-b

print(f"Результат: {result}")
print("Завершение программы...")

input()