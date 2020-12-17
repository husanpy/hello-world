#  You can experiment here, it won’t be checked

import random
import string


def generate_password(length, text):
    password = ''
    for _ in range(length):
        password += random.choice(text)
    return password


digits = string.digits
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
punctuation = '!#$%&*+-=?@^_'
chars = ''

pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
pwd_len = int(input('Какой длины должен быть пароль? '))
pwd_digits = input('Включать ли в пароль цифры? ')
pwd_uppercase = input('Включать ли в пароль прописные буквы? ')
pwd_lowercase = input('Включать ли в пароль строчные буквы? ')
pwd_punctuation = input(f'Включать ли в пароль символы "{punctuation}"? ')
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? ')

if pwd_digits == 'да':
    chars += digits
if pwd_lowercase == 'да':
    chars += lowercase_letters
if pwd_uppercase == 'да':
    chars += uppercase_letters
if pwd_punctuation == 'да':
    chars += punctuation
if pwd_exceptions == 'да':
    for el in 'il1Lo0O':
        chars = chars.replace(el, '')

print()
for i in range(pwd_quantity):
    print(f'Генерируем новый пароль длиной в {pwd_len} символов...')
    new_pass = generate_password(pwd_len, chars)
    print(f'Пароль №{i + 1}: {new_pass}')
    print()
   
