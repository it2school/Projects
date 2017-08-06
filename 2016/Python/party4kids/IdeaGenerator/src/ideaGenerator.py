from random import randint

first = ['Extreme', 'Random', 'Epic', 'Strange', 'Ultimate', 'Cool', 'Challenging', 'Easy', 'Impossible', 'Funny', 'Generic', 'Boring']
second = ['Dice', 'Life', 'Programming', 'Person', 'Fishing', 'Eating', 'Fighting', 'Idea', 'Car', 'Math', 'Minesweeper', 'Argument', 'Excuse', 'Hair', 'War', 'TV', 'Radio', 'Texting', 'Smartphone', 'Farming', 'Typing', 'Talking', 'Toilet', 'Sleeping', 'Spelling', 'Grammar', 'Driving', 'Thinking', 'Movie', 'Photo', 'Dancing', 'Bottle Flip', 'Video', 'Emoji', 'Biking', 'Music', 'Trivia', 'Book', 'Monster', 'Video', 'Hashtag', 'Airplane', 'Food', 'Politics', 'Planting', 'Stock Market', 'Sandwich', 'Business', 'Money', 'Baking', 'Build']
third = ['Simulator', 'Game' , 'Maker', 'Generator', 'Editor', 'Helper', 'Enigma', 'Puzzle', 'Thing', 'App', 'Website', 'Improver', 'Guide', 'Program', 'Project']

try:
    a = input('Сколько идей? ')
    a = int(a)
    if a > 99:
        raise ValueError
    print('~~~~Генерация~ ' + str(a) + ' ~идей~~~~')
    for i in range(a):
        n1 = randint(1, len(first)) - 1
        n2 = randint(1, len(second)) - 1
        n3 = randint(1, len(third)) - 1
        print("\n" + first[n1] + ' ' + second[n2] + ' ' + third[n3])
except:
    print('Ошибка: Недопустимое значение!')