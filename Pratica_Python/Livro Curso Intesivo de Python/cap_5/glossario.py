"""Um simples glossario."""

from collections import OrderedDict

glossario = OrderedDict()

glossario['Title'] = 'deixa a primeira letra maiúscula'
glossario['Str'] = 'torna o valor da string literal'
glossario['If'] = 'se o valor da condição for verdadeiro',
glossario['Elif'] = 'é executado se caso if for falso',
glossario['Else'] = 'normalmente executado após alguma string',
glossario['Set'] = 'seta o valor da variável',
glossario['Items'] = 'ordena os itens da lista',
glossario['Keys'] = 'escolhe as chaves da lista',
glossario['Values'] = 'escolhe os valores da lista',
glossario['Sort'] = 'ordena os itens da lista em ordem crescente'

for significado in glossario.items():
    print("\nSignificado: ", significado)
