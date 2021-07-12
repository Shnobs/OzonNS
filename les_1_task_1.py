year_of_birth = int(input('Введите год вашего рождения: '))
year_from_future = int(input('Введите год к которому расчитать возраст: '))
age = year_from_future - year_of_birth
print(f'Ваш возраст будет {age} лет')