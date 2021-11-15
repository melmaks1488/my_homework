def spam(number):

    return str('bulochka' * number)


def my_sum(list_of_numbers):


    pass
    i = 0
    list_len = len(list_of_numbers)
    s = 0

    while i <list_len:
        s += list_of_numbers[i]
        i += 1
    return s






def shortener(string):
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'


    """
    pass


    #  ...wite your code here
    stroka = (" ")
    return stroka.join(map(lambda trim: trim if len(trim) < 7 else trim[:6] + "*", string.split()))


def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    pass
    #  ...wite your code here
    summa = 0
    for i in words:
        str = ""
        if len(i) < 2:
            continue
        else:
            str += i
            if str[0] == str[-1]:
                summa += 1
    return summa



