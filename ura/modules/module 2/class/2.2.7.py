b = int(input())
q = b % 10
if q ==1 and b %100 != 11:
	print("бит")
elif q >=2 and q <= 4 and(b%100 < 10 or b %100 >=20):
	print("бита")
else:
	print("битов")
