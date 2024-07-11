num = input("Input number : ")
numMa = int(num)
L = ['*' for x in range(numMa)]
print(L)
for i in range(numMa + 1):
    if i != 0:
        print(' '.join(L[:i]))

for i in range(numMa, 0, -1):
    if i != 0:
        print(' '.join(L[:i]))

for i in range(0, numMa + 1):
    print(' ' * (numMa - i) + '* ' * i)
    #---------ตรงนี้คือสร้างช่องว่าง----ตรงนี้คือปริ้นจำนวน i
    #สร้างช่องว่างขึ้นมาตามการคำนวน numMa - i และปริ้นจำนวน i ของ"*""

for i in range(numMa, 0, -1):
    print(' ' * (numMa - i) + '* ' * i)

for i in range(1, numMa + 1):
    print(' ' * (numMa - i) + '*' * i)