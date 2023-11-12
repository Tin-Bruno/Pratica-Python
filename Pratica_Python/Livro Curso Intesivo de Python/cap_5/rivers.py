rivers = {'nilo': 'egito',
          'amazonas': 'peru',
          'yangtze': 'china'}
for river, local in rivers.items():
    print('\nThe ' + river.title() + ' passed in ' + local.title() + '.'
          + '\n', '\t' + river.title()
          + '\n', '\t' + local.title())
