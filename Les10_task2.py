import re
animals = ['питон', 'питон', 'кит', 'собака', 'питон', 'кит', 'кошка', 'горилла', 'кит', 'кошка', 'жираф',
           'леопард', 'жираф', 'жираф', 'кошка', 'горилла', 'жираф', 'жираф', 'кошка', 'жираф', 'кошка',
           'кошка', 'собака', 'кит', 'жираф', 'леопард', 'жираф', 'собака', 'кит', 'кит', 'кит', 'жираф',
           'собака', 'собака', 'кит', 'питон', 'леопард', 'кошка', 'жираф', 'собака', 'кошка', 'жираф',
           'кошка', 'собака', 'кит', 'леопард', 'леопард', 'горилла', 'горилла', 'кит']

regex = re.compile(r"\b[лк]\w+")
# Собираем регулярное выражение в отдельный объект (слово начинается с л или к, далее идут любые буквы
animals_filter = filter(regex.search, animals)  # Через функцию фильтер пропускаем список животных и условие фильтрации
print(list(animals_filter))  # Выводим получившийся список, преобразуем в List для вывода

animals_comprehension = [elem for elem in animals if re.findall(r"\b[лк]\w+", elem)]  # Проверяем каждый элемент списка
print(animals_comprehension)  # Выводим получившийся список
