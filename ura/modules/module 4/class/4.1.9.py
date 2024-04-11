def telephone(number):
    c = "0987654321+"
    a = True
    for i in number:
        if i not in c:
            a = False
            break
    if a:
        if len(number) == 12:
            if number[0] == "+" and number[1] == "7":
                a = True
            else:
                a = False
        else:
            a = False
    else:
        a = False
    print(a)