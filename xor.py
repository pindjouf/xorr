plaintext = []

with open("./yo.txt", "r") as f:
    file = f.read()
    for i in file:
        print(i)
        binary = bin(ord(i))[2:]
        plaintext.append(binary)

for i in range(len(plaintext)):
    while len(plaintext[i]) < 8:
        plaintext[i] = str(0) + plaintext[i]

for elem in plaintext:
    deci = int(''.join(map(str, elem)), 2)
    print(deci)
