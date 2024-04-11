b = int(input())
if b % 2 == 0:
    print('делится на 2')
if b % 3 == 0:
    print('делится на 3')
if b % 5 == 0:
    print('делится на 5')
if b % 7 == 0:
    print('делится на 7')
if b % 2 and b % 3 and b % 5 and b % 7 > 0:
    print('не делится на 2, 3, 5, 7')