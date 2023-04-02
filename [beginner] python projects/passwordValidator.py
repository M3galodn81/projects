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


print(password_length)
def ratePasswordLength():
    rate_password_length = ''
    if password_length <= 8:
        rate_password_length = ' 1️⃣ | Needs to be longer than 12 characters'
    if password_length >= 8 and password_length < 12:
        rate_password_length = ' 2️⃣ | Needs to be longer than 12 characters'
    if password_length >= 12 and password_length <16:
        rate_password_length = ' 3️⃣ | Good enough'
    if password_length >= 16:
        rate_password_length = ' 4️⃣ | Best'
    
    return rate_password_length

def ratePasswordVariety():
    rate_variety = ''
    rate_complexity = '
    if upperCase_numberChar < 1:
        rate_variety += f'No Upper Case Characters \n'
    if lowerCase_numberChar < 1:
        rate_variety += f'No Lower Case Characters \n'
    if numbers_numberChar < 1:
        rate_variety += f'No Numbers Characters \n'
    if symbols_numberChar < 1:
        rate_variety += f'No Symbol Characters \n'

    return rate_variety
print(ratePasswordLength())     