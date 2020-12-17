import random

rand_num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(num):
    flag = False
    if num.isdigit() and int(num) in range(1, 101):
        flag = True
    return flag

while True:
    num_inp = input('Введите число от 1 до 100:  ')
    if is_valid(num_inp):
        num = int(num_inp)
        if num < rand_num:
            print('Ваше число меньше заданного, попробуйте еще разок')
        elif num > rand_num:
            print('Ваше число больше заданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Хотите еще раз сыграть? Введите "да" или "нет"')
            if input().lower() == 'да':
                rand_num = random.randint(1, 100)
            else:
                break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
