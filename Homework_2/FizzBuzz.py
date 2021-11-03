
fizz = int(input("Enter the number fizz: "))
buzz = int(input("Enter the number buzz: "))
n = int(input("Enter the number n : "))
for x in (range(1, n + 1)):
    if x % fizz == 0 and x % buzz == 0:
        print(' FB ', end='')
    elif x % buzz == 0:
        print(" B ", end='')
    elif x % fizz == 0:
        print(" F ", end='')
    else:
        print(x, end='')
