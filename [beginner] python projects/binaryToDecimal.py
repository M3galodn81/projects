while True:
    try:
        binary_number = input('Enter a binary number: ')
        if not(len(binary_number) == 8):
            raise ValueError
        for x in binary_number:
            if not(x in ['0','1']):
                raise ValueError
        break
    except ValueError:
        print('Not a valid binary number')
        continue

print(f'Binary Number: {binary_number}')

binary_number = binary_number[::-1]
decimal_number = 0
for x in range(len(binary_number)):
    if binary_number[x] == '1':
        decimal_number += pow(2,int(x))

print(f'Decimal Number: {decimal_number}')