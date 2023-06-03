print("===" * 20)
print("Bem Vindo ao cadastro de usuários da P.G.G.")
print("===" * 20)

Funcionarios = []
users_accounts = []


def cadastro_pessoa(nome, idade, nascimento, logradouro, estado, nacionalidade, telefone, email, senha):
    cadastro_dic = {
        "Name": nome,
        "Age": idade,
        "Born": nascimento,
        "Public_place": logradouro,
        "State": estado,
        "Nationality": nacionalidade,
        "Telephone": telefone,
        "Email": email,
        "Password": senha
    }
    return cadastro_dic


while True:
    print("O que você deseja fazer?")
    print(""" [ Login ] \n[ Sing In ] \n [ Sair ]""")
    opcao = input("Sua escolha: ")

    if opcao == "Login":
        print("Informe seus dados de cadastro:")
        user_email = input("E-mail: ")
        user_senha = input("Senha: ")
    elif opcao == "Sing In":
        Name = input("Nome: ")
        Age = input("Idade: ")
        Born = input("Data de Nascimento: ")
        Public_place = input("Logradouro: ")
        State = input("Estado: ")
        Nationality = input("Nacionalidade: ")
        Telephone = input("Telefone: ")
        Email = input("E-mail: ")
        Password = input("Senha: ")

        dados_funcionario = cadastro_pessoa(
            Name, Age, Born, Public_place, State, Nationality, Telephone, Email, Password)
        Funcionarios.append(dados_funcionario)
    else:
        print("ENCERRANDO...")
        break

while True:
    print("Você deseja ver os dados dos funcionários?")
    print("""[ Sim ] \n[ Não ]""")
    opcao = input("Sua escolha: ")
    if opcao == "Sim":
        for funcionario in Funcionarios:
            print("===" * 20)
            for chave, valor in funcionario.items():
                print(f"{chave}: {valor}")
        break
    else:
        break
