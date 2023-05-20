data = {"name":'',
        "age": 0,
        "occupation": ''}

while True:
    try:
        name_input = input('Enter your name: ')
        if name_input != '':
            break
        raise ValueError
    except ValueError:
        continue

while True:
    try:
        age_input = input('Enter your age: ')
        age_input = int(age_input)
        break
    except ValueError:
        continue

while True:
    try:
        occupation_input = input('Enter your occupation: ')
        if occupation_input != '':
            break
        raise ValueError
    except ValueError:
        continue

data['name'] = name_input
data['age'] = age_input
data['occupation'] = occupation_input

f = open('test.txt','w')
f.writelines(str(data))
f.close()