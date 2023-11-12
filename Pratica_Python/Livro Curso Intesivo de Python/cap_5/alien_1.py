alien_0 = {'x': 0,
           'y': 0,
           'speed': 'fast'}
print("original x_position: "
      + str(alien_0['x']))
if alien_0['speed'] == 'slow':
    X = 1
    alien_0['x'] = alien_0['x'] + X
    print("new x_position: " + str(alien_0['x']))
elif alien_0['speed'] == 'medium':
    X = 2
    alien_0['x'] = alien_0['x'] + X
    print("new x_position: " + str(alien_0['x']))
else:
    alien_0['speed'] = 'fast'
    X = 3
    alien_0['x'] = alien_0['x'] + X
    print("new x_position: " + str(alien_0['x']))
