def F(n,m):
    if n % m == 0:
        return True
    return False
def A(s):
        for x in range(1,5000):

            a = F(45,s) and ((F(x,30)and F(x,12)) <= F(x,s))
            if not a:
                    return False
        return True
for i in range(1000,-1000,-1):
    if (A(i)):
        print(i)
        break
        
        