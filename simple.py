from __future__ import print_function
from pprint import pprint

a = 2
b = 0.5
print(a+b)

name = 'Дима'
print(f'Привет {name}')

v = int(input('Введите число от 1 до 10: '))
print(v+10)

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?')

print(float('1'))
print(int(2.5))
print(bool(1))
print(bool(''))
print(bool(0))

number_list = [3, 5, 7, 9, 10.5]
print(number_list)
number_list.append('Python')
print(len(number_list))

print(f'{number_list[0]} {number_list[-1]} {number_list[1:4]}')
number_list.remove('Python')

city_temperatue = {"city": "Москва", "temperature": 20}
print(city_temperatue['city'])
city_temperatue['temperature'] = city_temperatue['temperature'] - 5
pprint(city_temperatue)

city_temperatue.get('country')
city_temperatue.get('country', 'Россия')
city_temperatue['date'] = '27.05.2019'
print(city_temperatue)
print(len(city_temperatue))
