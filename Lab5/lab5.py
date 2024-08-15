class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def annual_salary(self):
        return super().annual_salary() + self.bonus

class Developer(Employee):
    def __init__(self, name, salary, projects):
        super().__init__(name, salary)
        self.projects = projects

    def annual_salary(self):
        bast_salary = self.salary * 12
        return  bast_salary + (self.projects * 1000)

# สร้าง object ของพนักงานแต่ละประเภท
manager = Manager("Alice", 6000, 5000)
developer = Developer("Bob", 5000, 3)

# คำนวณเงินเดือนประจำปีรวม
total_annual_salary = manager.annual_salary() + developer.annual_salary()

# แสดงผลลัพธ์
print( total_annual_salary )
