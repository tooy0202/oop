name = ["a", "b", "c"]
ages = [25, 30, 35]
city = ["New York", "Los Angeles", "thailand"]

for name, ages, city in zip(name,ages,city):
    #zip ทำให้สามารถวนได้พร้อมกัน
    print(f"{name} is {ages} years old and lives in {city}")
#f คือ แสดงค่าในตัวแปรแต่ละตัว