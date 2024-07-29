set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.add(5)
set2.discard(6)

print("Is set1 a subset of set2?", set1.issubset(set2))
#ตรวจสอบว่าเซต set1 เป็น subset ของเซต set2 หรือไม่ (คือ ทุกสมาชิกของ set1 อยู่ใน set2)
print("Is set2 a superset of set1?", set2.issuperset(set1))
#ตรวจสอบว่าเซต set2 เป็น superset ของเซต set1 หรือไม่ (คือ ทุกสมาชิกของ set1 อยู่ใน set2)