name = "Nitin"

for ch in name:
    print(ch)

#break and continue (skip the current iteration)
for i in range(1, 11):
    if i == 5:
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

i = 1

while i <= 5:
    print(i)
    i += 1

for i in range(5):
    pass