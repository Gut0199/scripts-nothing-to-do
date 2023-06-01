# Escalando um time de futebol.

users = []

while True:
    print("""Qual a opção que você quer escolher:
    [ 1 ] Adicionar Usuário:
    [ 2 ] Escalar Titulares:
    [ 3 ] Escalar Reservas:
    [ 4 ] Escalar o Técnico:
    [ 5 ] Comparar Escalações:
    [ 6 ] Sair """)
    your_chosen = input("Qual a sua escolha?: ")

    if your_chosen == "1":
        user_name = input("Digite o nome do usuário: ")
        users.append({
            'name': user_name,
            'titulares': [],
            'reservas': [],
            'tecnico': ''
        })
        print(f"Usuário '{user_name}' adicionado com sucesso!")
    elif your_chosen == "2":
        print("Hora de escalar o seu time Titular.")
        for user in users:
            print(f"--- Escalação de {user['name']} ---")
            soccer_players = []
            for soccer_player in range(1, 12):
                soccer_player_name = input("Digite o nome do jogador: ")
                soccer_player_position = input("Digite a posição do jogador: ")
                soccer_players.append([soccer_player_name, soccer_player_position])
            user['titulares'] = soccer_players
    elif your_chosen == "3":
        print("Hora de escalar os seus jogadores Reservas.")
        for user in users:
            print(f"--- Escalação de {user['name']} ---")
            reserves_players = []
            for reserve_player in range(1, 13):
                reserve_player_name = input("Digite o nome do jogador: ")
                reserve_player_position = input("Digite a posição do jogador: ")
                reserves_players.append([reserve_player_name, reserve_player_position])
            user['reservas'] = reserves_players
    elif your_chosen == "4":
        print("Certo, quer nomear o seu Técnico?")
        for user in users:
            print(f"--- Escalação de {user['name']} ---")
            tecnico_name = input("Digite o nome do seu Técnico: ")
            user['tecnico'] = tecnico_name
    elif your_chosen == "5":
        if len(users) < 2:
            print("Adicione pelo menos dois usuários para comparar as escalações.")
        else:
            for i in range(len(users) - 1):
                for j in range(i + 1, len(users)):
                    user1 = users[i]
                    user2 = users[j]
                    if user1['titulares'] == user2['titulares'] and user1['reservas'] == user2['reservas'] and user1['tecnico'] == user2['tecnico']:
                        print(f"As escalações de {user1['name']} e {user2['name']} são idênticas.")
                    else:
                        print(f"As escalações de {user1['name']} e {user2['name']} são diferentes.")
    else:
        break

print("Aqui está o plantel final de jogadores de cada usuário:")
for user in users:
    print(f"--- Escalação de {user['name']} ---")
    print("Titulares:")
    for player in user['titulares']:
        print(f"Nome: {player[0]}, Posição: {player[1]}")
    print("Reservas:")
    for player in user['reservas']:
        print(f"Nome: {player[0]}, Posição: {player[1]}")
    print("Técnico:")
    print(f"Nome do Técnico: {user['tecnico']}")
