games = ['tennis', 'chess', 'tag', 'pickle ball']
print("I like: ")
for game in games:
    print(game.title())

new_game = input("Please tell me a game you like: ")
games.append(new_game)

print("We like: ")
for game in games:
    print(game.title())
