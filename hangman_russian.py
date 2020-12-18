#  You can experiment here, it won’t be checked

#  You can experiment here, it won’t be checked

import random

words_list = ["человек", "слово", "лицо", "дверь", "земля",
              "работа", "ребенок", "история", "женщина", "развитие",
              "власть", "правительство", "начальник", "спектакль",
              "автомобиль", "экономика", "литература", "граница",
              "магазин", "председатель", "сотрудник", "республика",
              "личность"]


def get_word():
    return random.choice(words_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def print_w(text, list_chars):
    for char in text:
        if char in list_chars:
            print(char, end='')
        else:
            print('_', end='')
    print()


def play(word):
    # тело функции
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    while True:
        user_input = input('Введите букву или слово целиком:  ').upper()
        if not user_input.isalpha():
            print('Ошибка! Попробуйте еще...')
            continue
        if user_input in guessed_letters or user_input in guessed_words:
            print('Уже было. Попробуйте другой вариант')
            continue
        if len(user_input) > 1:
            if user_input == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
                print(word)
                break
            else:
                guessed_words.append(user_input)
                tries -= 1
                print(f'Увы, это не то слово. Осталось попыток: {tries}')
                print(display_hangman(tries))
                print_w(word, guessed_letters)
        elif user_input in word:
            guessed_letters.append(user_input)
            print(f'Поздравляем! Вы угадали букву {user_input}')
            for char in word:
                if char not in guessed_letters:
                    print_w(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:
                print('Поздравляем, вы угадали слово! Вы победили')
                print(word)
                break
        else:
            guessed_letters.append(user_input)
            tries -= 1
            print(f'Увы, этой буквы {user_input} нет в секретном слове.'
                  f'Осталось попыток: {tries}')
            print(display_hangman(tries))
            print_w(word, guessed_letters)
        if tries == 0:
            print(f'Увы, попытки кончились. Загаданное слово: {word}')
            break


play(get_word().upper())


