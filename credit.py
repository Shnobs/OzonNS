'''
name_1 = input('Введите имя: ')
name_2 = input('Введите имя: ')
name_3 = input('Введите имя: ')

salary_1 = input('Введите уровень дохода: ')
salary_2 = input('Введите уровень дохода: ')
salary_3 = input('Введите уровень дохода: ')
print(type(salary))
'''
credit = input('Введите сумму кредита: ')
period = input('Введите срок в месяцах: ')
procent = input('Введите процент: ')

pay_per_month = (int(credit)/ int(period) + int(credit)/100* int(procent)/12)
print(f'Платеж составит {pay_per_month} рублей в месяц')
print('Test git')