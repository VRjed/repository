h = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = 'abcdefghijklmnopqrstuvwxyz'
a = input()
b = ''
for i in a:
    if i in h or i in n:
        b += i
    else:
        continue
a = b.lower()
alphabet = {
    "a": "Alpha", "b": "Bravo", "c": "Charlie", "d": "Delta", "e": "Echo",
    "f": "Foxtrot", "g": "Golf", "h": "Hotel", "i": "India", "j": "Juliett",
    "k": "Kilo", "l": "Lima", "m": "Mike", "n": "November", "o": "Oscar",
    "p": "Papa", "q": "Quebec", "r": "Romeo", "s": "Sierra", "t": "Tango",
    "u": "Uniform", "v": "Victor", "w": "Whiskey", "x": "Xray", "y": "Yankee",
    "z": "Zulu"
}
g = ''
for i in a:
    d = alphabet.get(i,'')
    g += d + ' '
print(g)