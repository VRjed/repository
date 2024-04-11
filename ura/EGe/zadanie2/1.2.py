print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = (not(z) == (not(y))) or (not(x) and y) or w
                if a == False:

                
                    print(x, y , z ,w , a)




#(x ≡ ¬y) → ((z → ¬w) ∧ (w → y)).-