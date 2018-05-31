import random, string

letter_input = []
name_length = 4

for i in range(0, name_length):
    letter_input.append(input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other: '))

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
any = string.ascii_lowercase
name = ""

def generator():
    global name
    for i in letter_input:
        if i == "v":
            letter = random.choice(vowels)
        elif i == "c":
            letter = random.choice(consonants)
        elif i == "v":
            letter = random.choice(any)
        else:
            letter = letter_input
        name += letter

    return (name.title())

print(generator())
