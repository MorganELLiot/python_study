players = ['charlie', 'marina', 'michael', 'fiona', 'ella']
print(players[1:4:2])
print(players[3:])
print(players[-2:])
print('\n')
print('Here are the first 3 players:')
for player in players[:3]:
	print(player.title())