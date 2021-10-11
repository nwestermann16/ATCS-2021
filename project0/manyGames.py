games = ['tennis', 'chess', 'tag', 'pickle ball']
print("I like: ")
for game in games:
    print(game.title())

new_game = ''
while new_game != 'done':
    # Ask the user for a name.
    new_game = input("Please tell me a game you like, or enter 'done': ")

    # Add the new name to our list.
    if new_game != 'done':
        games.append(new_game)

print("We like: ")
for game in games:
    print(game.title())