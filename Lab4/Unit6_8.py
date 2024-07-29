set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1 | set2 #ยูเนียน (union) เซตที่รวมสมาชิกทั้งหมดของทั้งสองเซต โดยไม่ซ้ำกัน
intersection_set = set1 & set2 #อินเตอร์เซกชัน (intersection) เซตที่ประกอบด้วยสมาชิกที่ซ้ำกันในทั้งสองเซต
differnce_set = set1 - set2 #ดิฟเฟอเรนซ์ (difference) เซตที่ประกอบด้วยสมาชิกที่อยู่ใน set1 แต่ไม่อยู่ใน set2
symmetric_difference_set = set1 ^ set2 #ซิมเมตริกดิฟเฟอเรนซ์ (symmetric difference) เซตที่ประกอบด้วยสมาชิกที่อยู่ในเซตใดเซตหนึ่ง แต่ไม่อยู่ในทั้งสองเซต

print(union_set)
print(intersection_set)
print(differnce_set)
print(symmetric_difference_set)