#  You can experiment here, it won’t be checked
base_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
             '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def get_key(dic, value):
    for key, val in dic.items():
        if val == value:
            return key


def move_to_decs(num, base):
    num = num[::-1]
    dec_num = 0
    base_pow = 0
    for i in range(len(num)):
        dec_num += base_dict[num[i]] * (base ** base_pow)
        base_pow += 1
    return dec_num


def decs_to_base(num, base):
    num_str = ''
    while num > 0:
        num_str += get_key(base_dict, (num % base))
        num //= base
    return num_str[::-1]
