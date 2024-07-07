person = {'name':'Alice','age':30,'city':'New York'}

print("Name:", person['name'])

person['age'] = 31
print("Update age:", person['age'])

for key, value in person.items():
    print(f"{key}: {value}")

