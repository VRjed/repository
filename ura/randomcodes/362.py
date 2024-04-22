c = 0
for x in range(6,81):
    a = 5*x**4+5*x**3+1*x**2+1*x+3
    b = 7*80**3+x*80**2+x*80+5
    if abs(a-b) <= 1000000:
        c+=1
print(c)