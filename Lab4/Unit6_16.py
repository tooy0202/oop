list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

unique_elements = set(list1).union(set(list2)).difference(set(list3))
#set(list1).union(set(list2)): รวมเซต list1 และ list2 เข้าด้วยกัน
#.difference(set(list3)): ลบสมาชิกที่อยู่ใน list3 ออกจากผลรวมของ list1 และ list2 (5, 6, 7)
print("unique elements: ", unique_elements)