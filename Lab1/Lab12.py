cities = {
    'New York':[1,2,3,4,5,6],
    'Chaicago':[7,8,9,10,11,12],
    'thailand':[13,14,15,16,17,18]
}

av = {city:sum(temps)/len(temps) for city,temps in cities.items()}
print("Ave:",av)