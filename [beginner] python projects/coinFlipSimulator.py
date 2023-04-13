import random

coin = ['H','T']
while True:
    try:
        tries = input(f'How many tries would you like to simulated?: ')
        tries = int(tries)
        break
    except ValueError:
        print('Invalid Number')

result = []
for x in range(tries):
    index = random.randint(0,1)
    result.append(coin[index])

head_count = 0
tail_count = 0
for x in result:
    if x == 'H':
        head_count += 1
    else:
        tail_count += 1

print(result)
print(f'Heads: {head_count}, Tails : {tail_count}')


