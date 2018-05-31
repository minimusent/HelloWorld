import random, string

letter_input = []

for i in range(0, 4):
    letter_input.append(input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other: '))
    print(i)

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_lowercase

def generator():
    for i in letter_input:
        if letter_input == "v":
            letter[i] = random.choice(vowels)
        elif letter_input == "c":
            letter[i] = random.choice(consonants)
        elif letter_input == "v":
            letter[i] = random.choice(letter)
        else:
            letter[i] = letter_input
        name.append(letter[i])

    return (name)

print(generator())
