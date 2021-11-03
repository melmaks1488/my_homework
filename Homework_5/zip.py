def my_zip(*iterables):
    result = []
    args_lenths = []
    for iterable in iterables:
        args_lenths.append(len(iterable))
    min_length = min(args_lenths)
    for idx in range(min_length):
        iter_result = []
        for iterable in iterables:
            iter_result.append(iterable[idx])
        result.append(tuple(iter_result))

    return result

result = my_zip(["Maksym", "Sergey"], ['Meleshko'])
for first_name, last_name in result:
     print(first_name, last_name)