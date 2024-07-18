num = input("Input number : ")
numMa = int(num)
L = ['*' for x in range(numMa)]

def run():
    global numMa
    x = []
    y = []
    z = []
    o = []
    j = []

    for i in range(numMa + 1):
        if i != 0:
            x.append(' '.join(L[:i]))

    for i in range(numMa, 0, -1):
        if i != 0:
            y.append(' '.join(L[:i]))

    for i in range(0, numMa + 1):
        z.append(' ' * (numMa - i) + '* ' * i)

    for i in range(numMa, 0, -1):
        o.append(' ' * (numMa - i) + '* ' * i)

    for i in range(1, numMa + 1):
        j.append(' ' * (numMa - i) + '*' * i)
    
    return x, y, z, o, j #ตัวแปรต้องตรงกัน

#main-------------------------------------------------------------------------      
x, y, z, o, j = run() #ตัวแปรต้องตรงกัน
print()

print("------------")
for line in x:
    print(line)
print("------------")
for line in y:
    print(line)
print()

print("------------")
for line in z:
    print(line)
print("------------")
for line in o:
    print(line)
print()

print("------------")
for line in j:
    print(line)
print()