name = ['Fred', 'Jim', 'Bob']


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    for magician in magicians:
        print("The Great " + magician)


show_magicians(magicians=name)
make_great(magicians=name[:])
show_magicians(magicians=name)
