import copy

data = {'fname ': "Ganesh", 'lname': "Salunkhe", 'Age': 30, 'id': 25}

data1 = {'fname': "Ganesh", 'lname': "Salunkhe"}

data2 = {'Age': 30, 'id': 25}

finaldata = data1.copy()
finaldataa = data2.copy()
finaldatas = copy.copy(data1)
new_list = copy.deepcopy(data1)

print(finaldata)
print(finaldataa)
print(finaldatas)
print(new_list)




