players_list = [
  'Mario',
  'Kae',
  'Ronaldo Arruda',
  'José Vinícius',
  'Alex cavalcanti',
  'Gabriel Melo',
  'João Victor Rio',
  'Eduardo Cardoso',
  'Artur Sobral',
  'Gabriel Melo',
  'Bruno Mendonça',
  'João Cavalcanti',
  'Ivo Sales',
  'Rafael Sobral',
  'Arthur silva',
  'Victor Batista',
  'Bruno Mendonça',
  'Vitor Santos',
  'João Cavalcanti',
  'Rafael sobral',
  'João Guilherme',
  'Guilherme felicia',
  'Carlos Henrique',
  'Jean silva',
  'Lucas Matheus',
  'Jean wox',
  'Victor Batista',
  'Bruno Mendonça',
  'Matheus roberto',
  'Rafael Sobral',
  'Ivo Sales',
  'Gabriel Melo',
  'João Cavalcanti',
  'gabriel melo',
  'Daniel lira',
  'ivo sales',
]


def create_list(player_list):
  list_without_doubled = []
  for name in player_list:
    if not (name.lower() in list_without_doubled):
      list_without_doubled.append(name.lower())

  for i in range(len(list_without_doubled)):
    if i == 16:
      print('\nLISTA DE ESPERA')

    if i < 16:
      print(f'{i + 1} - {list_without_doubled[i]}')
    else:
      print(f'{i - 15} - {list_without_doubled[i]}')

create_list(players_list)
