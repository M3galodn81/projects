import random

range_min = 1 # inclusive
range_max = 11 # exclusive

random_list = list(range(range_min,range_max))

right_number = random.choice(random_list)

attempts = 0
while True:
    try:
        guess_number = input('Guess a number:')
        guess_number = int(guess_number)
        if not(guess_number in random_list):
            raise IndexError
        attempts += 1
        if guess_number == right_number:
            print(f'You took {attempts} attempts to guess {right_number}')
            break
    except ValueError:
        print(f'{guess_number} is not a valid number')
        continue
    except IndexError:
        print(f'{guess_number} is not inside the range of {range_min} to {range_max-1}')
        continue

print('Done')