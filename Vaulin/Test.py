# Задача 1. Переменные и типы данных
# 1. Создайте переменную `number` со значением 42.
# 2. Преобразуйте её в строку и сохраните в переменную `number_str`.
# 3. Создайте переменную `text` со значением "The answer is: ".
# 4. Объедините строку `text` и строку `number_str` и сохраните результат в переменную `result`.
# 5. Выведите на экран:
# - значение и тип данных `number`,
# - значение и тип данных `number_str`,
# - значение и тип данных `text`,
# - значение и тип данных `result`.

number = 42
number_str = str(number)

text = "The answer is: "

result = text + number_str

print(number, type(number))
print(number_str, type(number_str))
print(text, type(text))
print(result, type(result))

# Задача 2. Строки
# Даны две переменные:
# name = "внесите ваше имя сюда"
# age = введите ваш возраст.
# Используя f-строку, выведите на экран сообщение: "Меня зовут ваше имя, мне ваш возраст лет."

name = "Алексндр"
age = 35

info = f"Меня зовут {name}, мне {age} лет"

print(info)

# Задача 3. Списки
# Дан список my_list = [1, 2, 3].
# Создайте копию этого списка, измените первый элемент копии на 10 и выведите оба списка.

my_list = [1, 2, 3]

my_list_new = my_list.copy()
my_list_new[0] = 10

print(my_list)
print(my_list_new)


# Задача 4. Условные операторы
# Напишите программу, которая принимает число от пользователя и проверяет:
# - Если число больше 0, выведите "Положительное".
# - Если число равно 0, выведите "Ноль".
# - Если число меньше 0, выведите "Отрицательное".

number = int(input("Введите число: "))

if number > 0:
    print("Положительное")
elif number == 0:
    print("Ноль")
else:
   print("Отрицательное")

# Задача 5. Словари
# Дан словарь:
#
# person = {
#
#       "name": {
#
#           "first_name": "Иван",
#
#           "last_name": "Иванов"
#
# },
#
#    "address": {
#
#        "city": "Москва",
#
#       "country": "Россия"
#
#     }
#
# }
#
# Обновите значение ключа "city" на "Санкт-Петербург" и добавьте новый ключ "postal_code" со значением "333777" в словарь "address".
# Выведите значение через print.
# Затем удалите ключ "city" из вложенного словаря "address" и снова выведите значение через print.


person = {
    "name": {
        "first_name": "Иван",
        "last_name": "Иванов"
    },
    "address": {
        "city": "Москва",
        "country": "Россия"
    }
}

person["address"]["city"] = "Санкт-Петербург"

person["address"]["postal_code"] = "333777"

print(person)

del person["address"]["city"]

print(person)

# Задача 6. Циклы
#
# Напишите цикл while, который выводит числа от 1 до 20, но пропускает числа, которые делятся на 4 (используйте continue)

number = 1

while number <= 20:

    if number % 4 == 0:
        number += 1
        continue

    print(number)
    number += 1

# Задача 7. Файлы
# Создайте файл с именем "fruits.txt" и запишите в него названия фруктов:
# "яблоко", "банан", "апельсин" (каждое с новой строки).
# Затем откройте этот файл, прочитайте все строки и выведите на экран только те строки, которые начинаются с буквы "а".

file = open("fruits.txt", "w", encoding='utf-8')

file.write("\nяблоко")
file.write("\nбанан")
file.write("\nапельсин")

file.close()

file = open("fruits.txt", "r", encoding='utf-8')
lines = file.readlines()
file.close()

for line in lines:
    if line.startswith("а"):
        print(line)

# Задача 8. Функции
# Напишите функцию greet_user, которая приветствует пользователя в зависимости от его роли и имени. Функция должна принимать два параметра:
# user_role (обязательный) — строка, указывающая роль пользователя (например, "Администратор", "Гость", "Модератор").
# user_name (необязательный) — строка с именем пользователя. По умолчанию должно быть None.
# Логика работы функции:
# - Если имя пользователя передано (user_name не None и не пустая строка), функция должна вывести: "Привет, {user_name}! Ваша роль: {user_role}."
# - Если имя не передано (user_name равно None или пустая строка), функция должна вывести: "Привет, Гость! Ваша роль: {user_role}."

def greet_user(user_role, user_name=None):
    if user_name and user_name.strip():  # Проверяем, что имя не None и не пустая строка
        print(f"Привет, {user_name}! Ваша роль: {user_role}.")
    else:
        print(f"Привет, Гость! Ваша роль: {user_role}.")

greet_user("Администратор", "Анна")
greet_user("Модератор")  # user_name не передан, используется None
greet_user("Гость", "")  # Пустая строка
greet_user("Администратор", "   ")  # Строка из пробелов

# Задача 9. ООП ч.1
# Создайте класс `Student`.
# У класса должны быть атрибуты `name`  и `age`, которые задаются при создании объекта через конструктор `__init__`.
# Создай объект класса `Student` с вашим именем и вашим возрастом.
# Выведи на экран имя и возраст студента.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Student("Александр", 35)

print(f"Имя: {person1.name}, Возраст: {person1.age}")


# Задача 10. ООП ч.2
# Создайте класс Animal с атрибутами:
# name (кличка животного)
# species (вид животного, например "собака")
# И методами:
# eat()
# sleep()
# Затем создайте дочерний класс Dog, который:
# Наследует все от класса Animal
# Имеет дополнительный метод bark() (лаять)
# Задание:
# - Создайте объект my_dog класса Dog с любым именем
# - Вызовите все три метода eat(), sleep(), bark() и выведите результаты

class Animal:
    def __init__(self, name, species):
        self.name = name
        self. species = species

    def eat(self):
        print(f"{self.name} ест")

    def sleep(self):
            print(f"{self.name} спит")

class Dog(Animal):
        def bark(self):
            print(f"{self.name} лает: Гав-гав!")

my_dog = Dog("Бобик", "собака")

my_dog.eat()
my_dog.sleep()
my_dog.bark()





