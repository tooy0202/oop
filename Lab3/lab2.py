numS = input("Input number: ")
num = int(numS)
L = ['*' for x in range(num)]
onetomax = 0
count = 0

def main_():
    global onetomax
    global num

    # รีเซ็ต onetomax และ count ก่อนการเรียกใช้แต่ละครั้ง
    onetomax = 0
    count = 0

    x = print_numbers1(onetomax) #ทั้งหมดนี้จะถูกสร้างให้เป็น list
    y = print_numbers2(num)
    z = print_numbers3(onetomax)
    o = print_numbers4(num)
    j = print_numbers5(onetomax)

    return x, y, z, o, j #ตัวแปรต้องตรงกัน

def print_numbers1(onetomax):
    global num
    result = []
    if onetomax > num:
        return result
    if onetomax != 0:
        result.append(' '.join(L[:onetomax]))#สร้างตัวของดอกจันตามจำนวน onetomax และใช้ join ทำให้ L[:onetomax] เป็นสตริงเดียวและเก็บค่าใน result = []
    result.extend(print_numbers1(onetomax + 1)) #extend จะเพิ่มหลายองค์ประกอบจาก iterable เข้าไปในลิสต์ทีเดียว
    return result

def print_numbers2(num):
    result = []
    if num < 0:
        return result
    if num != 0:
        result.append(' '.join(L[:num]))
    result.extend(print_numbers2(num - 1))
    return result

def print_numbers3(onetomax):
    global num
    result = []
    if onetomax > num:
        return result
    result.append(' ' * (num - onetomax) + '* ' * onetomax)
    result.extend(print_numbers3(onetomax + 1))
    return result

def print_numbers4(num):
    global count
    result = []
    numM = num - count
    if numM < 0:
        return result
    result.append(' ' * (num - numM) + '* ' * numM)
    count += 1
    result.extend(print_numbers4(num))
    return result

def print_numbers5(onetomax):
    global num
    result = []
    if onetomax >= num:
        return result
    result.append(' ' * (num - onetomax) + '*' * (onetomax + 1))
    result.extend(print_numbers5(onetomax + 1))
    return result

x, y, z, o, j = main_() #ตัวแปรต้องตรงกัน

print()
print("------------")
for line in x:
    print(line)
print("------------")
for line in y:
    print(line)
print() #บรรทัดว่าง

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