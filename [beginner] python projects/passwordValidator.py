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
    password_rating = 0
    rate_password_length = ''
    if password_length <= 8:
        rate_password_length = 'Needs to be longer than 12 characters\n'
        password_rating += 1
    if password_length >= 8 and password_length < 12:
        rate_password_length = 'Needs to be longer than 12 characters\n'
        password_rating += 2
    if password_length >= 12 and password_length <16:
        rate_password_length = 'Good enough\n'
        password_rating += 3
    if password_length >= 16:
        rate_password_length = 'Best\n'
        password_rating += 4
    return rate_password_length,password_rating

def ratePasswordVariety():
    password_rating = 4
    rate_variety = ''
    if upperCase_numberChar < 1:
        rate_variety += f'No Upper Case Characters \n'
        password_rating -= 1
    elif lowerCase_numberChar < 1:
        rate_variety += f'No Lower Case Characters \n'
        password_rating -= 1
    elif numbers_numberChar < 1:
        rate_variety += f'No Numbers Characters \n'
        password_rating -= 1
    elif symbols_numberChar < 1:
        rate_variety += f'No Symbol Characters \n'
        password_rating -= 1
    else:
        rate_variety += f'Best variety of characters\n'
    return rate_variety,password_rating

def ratePasswordComplexity():
    password_rating = 0
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
        password_rating += 1
    if repeated_type < (0.25 * password_length):
        rate_complexity += f'Password is very complex'
        password_rating += 2
    return rate_complexity,password_rating


print(f'Length: {ratePasswordLength()[1]} / 4')
print(ratePasswordLength()[0])

print(f'Variety: {ratePasswordVariety()[1]} / 4')
print(ratePasswordVariety()[0])

print(f'Complexity: {ratePasswordComplexity()[1]} / 2')
print(ratePasswordComplexity()[0])

print(f'Rating: {ratePasswordComplexity()[1] + ratePasswordLength()[1] + ratePasswordVariety()[1]} / 10')