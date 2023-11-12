def make_album(name, music, number=''):
    album = {'Artist': name, 'album': music}
    if number:
        album['album_number'] = number
    return album


while True:
    print("\nPlease enter your favorite artist and music:")
    print("Digit 'Q' to quit.")
    artist = input("\nArtist: ")
    if artist.lower() == 'q':
        break

    music_question = input("music: ")
    if music_question.lower() == 'q':
        break

    print("\n_________Resuts_________")
    print(make_album(artist, music_question))
    album_1 = make_album(name='Bob', music='Is this love', number=str(1))
    album_2 = make_album(name='Beatles', music='Birtday')
    album_3 = make_album(name='Imagine Dragons', music='Belivier')
    print(album_1)
    print(album_2)
    print(album_3)
