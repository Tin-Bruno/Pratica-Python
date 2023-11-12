invite = ['fag', 'lucas', 'bruno',]
invite.insert(0, 'gabriel')
invite.insert(1, 'michael')
invite.append('saulo')
invite.pop()
invite.pop()
invite.pop()
invite.pop()
invite_len = len(invite)
print('olá, '
      + (invite[0].title())
      + ' wonld  would to go a dinner in weekend'
      )
print('olá, '
      + (invite[1].title())
      + ' wonld  would to go a dinner in weekend'
      )
print("\nkaio can't going a dinner in weekend")
print("\nI got a bigger table")
print("\ni can to invite only two persons")
print("\ninvited persons: " + str(invite_len))
