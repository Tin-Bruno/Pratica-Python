video_games = ['ps4', 'xbox x', 'nintendo']
video_games.append('ps3')
video_games.insert(0, 'xbox')
popped_video_games = video_games.pop(0)
print('video game popped:' + str(popped_video_games))
del video_games[0]
video_games.remove("nintendo")
video_games.sort()
video_games.reverse()
video_games_len = len(video_games)
print('\nvideo games i wish i had ' + str(video_games))
print('\nnumber to video games: ' + str(video_games_len))
