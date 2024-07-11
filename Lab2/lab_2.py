numS = input("Input number : ")
num = int(numS)
L = ['*' for x in range(num)]
onetomax = 0
count = 0
def print_numbers1(onetomax):
    if onetomax > num:
        return
    if onetomax != 0:
        print(' '.join(L[:onetomax]))
    print_numbers1(onetomax + 1)
    ##เรียกใช้ครั้งที่ 2 เพื่อให้เกิดลูป

def print_numbers2(num):
    if onetomax > num:
        return
    if num != 0:
        print(' '.join(L[:num]))
    print_numbers2(num - 1)

def print_numbers3(onetomax):
    if onetomax > num:
        return
    
    print(' ' * (num - onetomax) + '* ' * onetomax)
    print_numbers3(onetomax + 1)

def print_numbers4(num):
    global count
    numM = num-count
    if numM < 0:
        return
    
    print(' ' * (num - numM) + '* ' * numM)
    count += 1
    print_numbers4(num)

def print_numbers5(onetomax):
    if onetomax > num:
        return
    print(' ' * (num - onetomax) + '*' * (onetomax + 1))
    print_numbers5(onetomax + 1)

##เรียกใช้ครั้งที่ 1
print_numbers1(onetomax)
print("-----------")
print_numbers2(num)
print("-----------")
print_numbers3(onetomax)
print("-----------")
print_numbers4(num)
print("-----------")
print_numbers5(onetomax)