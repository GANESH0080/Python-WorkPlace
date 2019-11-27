data = {'fname': "Ganesh", 'lname': "Salunkhe", 'id': 30, 'rollnumber': 55};

names = {'fname': "Ganesh", 'lname': "Salunkhee", 'id': 60};

for key in data.keys():

    if key in names.keys():
        print("true")
    else:
        print("false")
