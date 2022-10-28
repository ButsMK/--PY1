def get_count_char(str_):
    out = {}
    str_ = str_.lower() # TODO посчитать количество каждой буквы в строке в аргументе str_
    for i in str_:
        if i.isalpha():
            if i in out:
                out[i] += 1
            else:
                out[i] = 1
    return out


def get_perc_char(dict_: dict):
    new_dict = dict_.copy()
    total = sum(new_dict.values())
    for i in new_dict:
        new_dict[i] = new_dict[i]/total * 100
    return new_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
