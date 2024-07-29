stack = []
stack.append(1)
stack.append(2)
stack.append(3)
popped_item = stack.pop()#pop ค่าสูงสุดเก็บใน popped_item
print("Poped item from stack: ", popped_item)#สุดท้ายจะเป็น 3
#สแต็ก เป็นโครงสร้างข้อมูลแบบ LIFO (Last In, First Out) หมายความว่าค่าสุดท้ายที่ใส่เข้าไปจะเป็นค่าแรกที่เอาออก

from collections import deque #เพื่อใช้สร้างคิว
queue = deque([1, 2, 3])
queue.append(4)
dequeued_item = queue.popleft() #เอาค่าตัวแรกออกจากคิว
print("Dequeued item from queue: ", dequeued_item)
#คิว เป็นโครงสร้างข้อมูลแบบ FIFO (First In, First Out) หมายความว่าค่าแรกที่ใส่เข้าไปจะเป็นค่าแรกที่เอาออก