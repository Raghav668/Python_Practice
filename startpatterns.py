
for r in range(1,5):
    for c in range (1,5):
        print("#", end=" ")
    print()

print()

for r in range(1,5):
    for c in range (r):
        print("#", end=" ")
    print()
print()

for r in range(4):
    for c in range (4-r):
        print("#", end=" ")
    print()
print()

for r in range(1,5):
    for c in range (r,5):
        print(c, end=" ")
    print()