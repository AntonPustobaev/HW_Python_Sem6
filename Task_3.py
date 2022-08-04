# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах


def input_rle():
    with open('input.txt', 'r', encoding='utf-8') as file:
        data = list(map(str.strip, file.readlines()))
    lst = []
    for i in data:
        count = 1
        string = ''
        symbol = i[0]
        for k in range(1, len(i)):
            new_symbol = i[k]
            if new_symbol == symbol:
                count += 1
            else:
                string += symbol if count == 1 else str(count) + symbol
                symbol = i[k]
                count = 1
        string += symbol if count == 1 else str(count) + symbol
        lst.append(string)
    with open('output.txt', 'w', encoding='utf-8') as file:
        for i in lst:
            print(i, file=file)
    return lst


def output_rle():
    with open('output.txt') as file:
        data = list(map(str.strip, file.readlines()))
    lst = []
    for i in data:
        string = ''
        time_string = ''
        for k in i:
            if k.isdigit():
                time_string += k
            else:
                string += k if time_string == '' else int(time_string) * k
                time_string = ''
    lst.append(string)
    return lst


print(f'сжатие {input_rle()}: ')
print(f'восстановление {output_rle()} ')