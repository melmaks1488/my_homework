from random import randint

stud_list = {
    "Kircha Otdihayu": [randint(1,10) for i in range(15)],
    "Herbin Evgeniy": [randint(1,10) for a in range(15)],
    "Dyadya Knur": [randint(1,10) for b in range(15)],
    "Dima Kytsenko": [randint(1,10) for c in range(15)],
    "Sasha Samoilov": [randint(1,10) for d in range(15)],
    "Timofey Anime": [randint(1,10) for e in range(15)]
}

def mean(lst):
    return sum(lst) / len(lst)

sortedIds = sorted(list(stud_list.keys()), key=lambda studentId: mean(stud_list[studentId]))

print('The best student:', sortedIds[-1])
print('Worst student:', sortedIds[0])