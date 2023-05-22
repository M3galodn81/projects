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

f = open('test.txt','w') # create a file and write on it
f.writelines(str(data))
f.close()

r = open('test.txt','r')  #reads
print(r.read())
r.close()

import os

if os.path.exists('test.txt'):
    os.remove('test.txt')
    print('Removed test.txt')
else:
    print('The file does not exist')