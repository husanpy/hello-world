def is_valid_text(text):
    flag = False
    if text != '':
        flag = True
    return flag


def is_valid(text, var1, var2):
    flag = False
    if text in [var1, var2]:
        flag = True
    return flag


def is_valid_digit(num):
    flag = False
    if num.isdigit() and float(n) % int(n) == 0:
        flag = True
    return flag


def caesar_cif(text, k, language, operation):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    new_text = ''

    if language == 'en':
        if operation == 'ch':
            for i in range(len(text)):
                # ENG CIF
                if text[i].isalpha():
                    if text[i].isupper():
                        upp_index = eng_upper_alphabet.find(text[i])
                        if (upp_index + k) < len(eng_upper_alphabet):
                            up_cif_ind = upp_index + k
                        else:
                            up_cif_ind = upp_index + k - len(eng_upper_alphabet)
                        new_text += eng_upper_alphabet[up_cif_ind]
                    elif text[i].islower():
                        low_index = eng_lower_alphabet.find(text[i])
                        if (low_index + k) < len(eng_lower_alphabet):
                            low_cif_ind = low_index + k
                        else:
                            low_cif_ind = low_index + k - len(eng_lower_alphabet)
                        new_text += eng_lower_alphabet[low_cif_ind]
                else:
                    new_text += text[i]
        else:
            k = -k
            for i in range(len(text)):
                # ENG DEF
                if text[i].isalpha():
                    if text[i] == text[i].upper():
                        upp_index = eng_upper_alphabet.find(text[i])
                        up_def_ind = upp_index + k
                        new_text += eng_upper_alphabet[up_def_ind]
                    elif text[i] == text[i].lower():
                        low_index = eng_lower_alphabet.find(text[i])
                        low_def_ind = low_index + k
                        new_text += eng_lower_alphabet[low_def_ind]
                else:
                    new_text += text[i]
    else:
        if operation == 'ch':
            for i in range(len(text)):
                # RUS CIF
                if text[i].isalpha():
                    if text[i] == text[i].upper():
                        upp_index = rus_upper_alphabet.find(text[i])
                        if (upp_index + k) < len(rus_upper_alphabet):
                            up_cif_ind = upp_index + k
                        else:
                            up_cif_ind = upp_index + k - len(rus_upper_alphabet)
                        new_text += rus_upper_alphabet[up_cif_ind]
                    elif text[i] == text[i].lower():
                        low_index = rus_lower_alphabet.find(text[i])
                        if (low_index + k) < len(rus_lower_alphabet):
                            low_cif_ind = low_index + k
                        else:
                            low_cif_ind = low_index + k - len(rus_lower_alphabet)
                        new_text += rus_lower_alphabet[low_cif_ind]
                else:
                    new_text += text[i]
        else:
            k = -k
            for i in range(len(text)):
                # RUS DEF
                if text[i].isalpha():
                    if text[i] == text[i].upper():
                        upp_index = rus_upper_alphabet.find(text[i])
                        up_def_ind = upp_index + k
                        new_text += rus_upper_alphabet[up_def_ind]
                    elif text[i] == text[i].lower():
                        low_index = rus_lower_alphabet.find(text[i])
                        low_def_ind = low_index + k
                        new_text += rus_lower_alphabet[low_def_ind]
                else:
                    new_text += text[i]

    return new_text


text = input('Введите исходный текст:  ')
while True:
    if is_valid_text(text):
        break
    else:
        text = input('Пожалуйста, введите текст:  ')

operation = input('Выберите направление: шифрование - введите "ch" или дешифрование - введите "def":    ')
while True:
    if is_valid(operation, 'ch', 'def'):
        break
    else:
        operation = input('Пожалуйста, введите "ch" или "def": шифрование - "ch", дешифрование - "def":    ')

language = input('Выберите язык алфавита: английский - "en", русский - "rus":  ')
while True:
    if is_valid(language, 'en', 'rus'):
        break
    else:
        language = input('Пожалуйста, введите "en" или "rus": английский - "en", русский - "rus":    ')

by_word = input('Универсальный шаг или для каждого слова по длине слова? У/С:  ')
while True:
    if by_word in 'yYуУ':
        n = input('Введите целое число - шаг сдвига:  ')
        while True:
            if is_valid_digit(n):
                n = int(n)
                break
            else:
                n = input('Пожалуйста, введите целое число - шаг сдвига:  ')

        if language == 'en':
            print('Modified text...')
        else:
            print('Обработанный текст...')
        print(caesar_cif(text, n, language, operation))
        break

    elif by_word in 'cCсС':
        list_words = text.split()
        new_list = []

        for el in list_words:
            num = 0
            for c in el:
                if c.isalpha():
                    num += 1
            new_list.append(caesar_cif(el, num, language, operation))

        if language == 'en':
            print('Modified text...')
        else:
            print('Обработанный текст...')
        print(' '.join(new_list))
        break

    else:
        by_word = input('Введите либо У (от слова У-ниверсальный, либо С (по С-лову) У/С:  ')
