tm = []
while n := int(input()):
    tm.append(n)

print(len([i for i in range(len(tm) - 1) if tm[i + 1] > tm[i]]))
