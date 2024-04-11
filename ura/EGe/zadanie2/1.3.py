#((x → y ) ≡ (z → w)) ∨ (x ∧ w).
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = ((x <= y ) == (z <= w)) or (x and w)
                print(x, y , z ,w , a)
            #((x → y ) ≡ (z → w)) ∨ (x ∧ w).