import random
import time
import os

def game():
    print('''Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n''', end = ' ')

    #Выбор сложности
    difficulty = ''
    while difficulty not in ['1', '2', '3', 'easy', 'medium', 'hard']:
        print('\nEnter your choice CORRECTLY:', end = ' ')
        difficulty = input().lower().strip()

    if difficulty in ['1', 'easy']:
        print('Great! You have selected the Easy difficulty level.')
        chances = 10
    elif difficulty in ['2', 'medium']:
        print('Great! You have selected the Medium difficulty level.')
        chances = 5
    elif difficulty in ['3', 'hard']:
        print('Great! You have selected the Hard difficulty level.')
        chances = 3
    print()
    #Выбор числа
    target = random.randint(1, 100)
    print('So, the number is guessed.')

    #Начало игры
    start = time.time() #Начинаем отсчет времени
    score = float('inf')
    guess = 0

    for i in range(1, chances+1):
        #Пользователь вводит число
        while guess == 0:
            try:
                guess = int(input('Enter your guess >> '))
            except ValueError:
                print('Please try again.\n')

        # Угадал
        if guess == target:
            score = i
            print(f'Correct! You guessed the correct number in {score} attempts.')
            break

        #Не угадал
        elif guess < target:
            print(f'Incorrect! The number is greater than {guess}.')
        elif guess > target:
            print(f'Incorrect! The number is less than {guess}.')

        print()
        guess = 0

    #Заканчиваем отсчет времени
    end = time.time()
    duration = round(end - start, 2)

    #Попытки закончились
    if guess != target:
        print(f"You couldn't guess the number. It was {target}.")

    #Отображение, сколько по времени заняло угадывание
    print(f'It took about {duration} seconds to guess the number.')
    print()

    #Берем время и попытки, записанное в файле и сравниваем с тем, что у пользователя
    path = os.path.expanduser('results.txt')
    try:
        with open(path, 'r+') as f:
            read = f.read().strip().split(' ')
            try:
                min_score, min_time = map(float, read)
            except ValueError:
                min_score, min_time = score, duration

            if min_score > score: min_score = score
            if min_time > duration: min_time = duration

            f.seek(0)
            f.truncate(0)
            f.write(str(min_score)+' '+str(min_time))

    except FileNotFoundError:
        print("Oh, you're playing for the first time.")
        min_score, min_time = score, duration
        with open(path, 'w') as f:
            f.write(str(min_score)+' '+str(min_time))


    #Хочет ли пользователь еще раз поиграть
    if input('Do you want to play again? (y/n) >> ').strip().lower() == 'y':
        print()
        game()
    else:
        print()
        print('Goodbye!')
        exit()


if __name__ == '__main__':
    # Приветствие
    print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
''')
    game()
