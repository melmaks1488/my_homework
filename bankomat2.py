s = int(input("please enter summu for get \n")) #сумма, которую хотят получить
if s < 20:
    print("bomzhara")
    if s % 20 !=0:
        print("введи корректную сумму")

denominations = [1000, 500, 200, 100, 50, 20]

bills = list()

for denominations in denominations:
    bill_c = s // denominations
    if not bill_c:
        continue

    bills.append((denominations, bill_c))
    s %= denominations
for denominations, bill_c in bills:
    print(denominations, "x", bill_c)











