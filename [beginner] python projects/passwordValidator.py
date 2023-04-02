import string
punctuation = string.punctuation
password = input('Enter the password: ')

upperCase_numberChar = 0
lowerCase_numberChar = 0
numbers_numberChar = 0
symbols_numberChar = 0
password_length = 0

for i in password:
    if i.isupper():
        upperCase_numberChar += 1
    if i.islower():
        lowerCase_numberChar += 1
    if i.isnumeric():
        numbers_numberChar += 1
    if any(char in punctuation for char in i):
        symbols_numberChar += 1
    password_length += 1

# print(password_length)

def ratePasswordLength():
    rate_password_length = ''
    if password_length <= 8:
        rate_password_length = 'Needs to be longer than 12 characters'
    if password_length >= 8 and password_length < 12:
        rate_password_length = 'Needs to be longer than 12 characters'
    if password_length >= 12 and password_length <16:
        rate_password_length = 'Good enough'
    if password_length >= 16:
        rate_password_length = 'Best'
    
    return rate_password_length

def ratePasswordVariety():
    rate_variety = ''
    if upperCase_numberChar < 1:
        rate_variety += f'No Upper Case Characters \n'
    if lowerCase_numberChar < 1:
        rate_variety += f'No Lower Case Characters \n'
    if numbers_numberChar < 1:
        rate_variety += f'No Numbers Characters \n'
    if symbols_numberChar < 1:
        rate_variety += f'No Symbol Characters \n'

    return rate_variety

def ratePasswordComplexity():
    rate_complexity = ''
    password_type = []
    for char in password:
        if char.isupper():
            password_type.append(0)
        if char.islower():
            password_type.append(1)
        if char.isnumeric():
            password_type.append(2)
        if any(i in punctuation for i in char):
            password_type.append(3)
    # print(password_type)

    char_type:int = None
    repeated_type = 0
    for x in range(len(password_type)):
        # print(char_type,password_type[x])
        if char_type == password_type[x]:
            repeated_type += 1
        char_type = password_type[x]
    if repeated_type >= (0.5 * password_length):
        rate_complexity += f'Password has mutliple similar characters'
    if repeated_type >= (0.25 * password_length) and repeated_type < (0.50 * password_length):
        rate_complexity += f'Password is complex enough'
    if repeated_type < (0.25 * password_length):
        rate_complexity += f'Password is very complex'

    return rate_complexity


print(f'Length:')
print(ratePasswordLength())

print(f'Variety:')
print(ratePasswordVariety())

print(f'Complexity:')
print(ratePasswordComplexity())