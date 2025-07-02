countries = ("Spain", "Italy", "India", "England","Germany")
temp = list(countries)
temp.append("Russia")  #add item
temp.pop(3)  #remove item
temp[3] = "Finland"  #change item
countries = tuple(temp)
print(countries)