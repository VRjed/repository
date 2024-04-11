for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = ((x <= y ) and (y <= w)) or (z == ( x or y))
                print (x, y , z, w , a)
#((x → y ) ∧ (y → w)) ∨ (z ≡ ( x ∨ y)).