import Les5_task2_1 as mf  # Импортируем функции из файла Les5_task2_1.py
shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}
spisok = mf.shows_janr(shows, 'драма')  # Создаем список ключей по заданному значению
print(f' Сериалы {str(spisok)[1:-1]} имеют средний рейтинг {mf.ratings_janr(ratings, spisok)}')   # Выводим результат
spisok2 = mf.shows_janr(shows, 'криминал')  # Создаем список ключей по заданному значению
print(f' Сериалы {str(spisok2)[1:-1]} имеют средний рейтинг {mf.ratings_janr(ratings, spisok2)}')  # Выводим результат
