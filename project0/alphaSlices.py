smallAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
firstLetters = smallAlpha[0:3]
for letter in firstLetters:
    print(letter.title())

firstLetters = smallAlpha[0:3]
for letter in firstLetters:
    print(letter.title[5:8])

firstLetters = smallAlpha[0:3]
for letter in firstLetters:
    print(letter.title[7:])
