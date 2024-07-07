squares = [x**2 for x in range(10)]
#x คือ 1-10 และ ทั้งหมด ยกกำลัง 2
squares_dict = {
    x: x**2 for x in range(5)
}
#x: คือจำนวนรอบ
even_squares = {
    xx**2 for xx in range(10) if xx % 2 == 0
}

print(squares)
print(squares_dict)
print(even_squares)