data ={'Alice': 'Female', 
       'Bob': 'Male',
        'Carol': 'Male'}

def update():
    name = input (" Enter the name :")
    for key in data.keys():
        if key == name:
            new_name = input('Enter the new name, empty for no change:')
            if new_name == '':
                new_name = name
            while not new_name.istitle():
                new_name = input('Wrong input, please re-enter :')
            data[new_name] = data.pop(key)
            new_gender = input('Enter the new gender, empty for no change :')
            if new_gender == '':
                new_gender =data[key]
            while new_gender not in ['Male', 'Female']:
                new_gender = input('Wrong input, please re-enter:')
            data[key] = new_gender
            
            print(new_name, 'updated.')
            print(data)
            return

    print(name + 'is not in the data base. Operation failed.')
