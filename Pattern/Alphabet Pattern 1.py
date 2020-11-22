"""
    A
    B B
    C C C
    D D D D
    E E E E E
"""
i = j = 1
for i in range(1, 6):
    print()
    for j in range(65, 65+i):
        print(chr(64+i), end=" ")
