def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a + b

f = fib()
print(next(f)) #ทำงานร่วมดับ yield เป็นการส่งค่า a ออกมา
print(next(f))