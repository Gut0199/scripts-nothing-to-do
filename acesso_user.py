print("-="*20)
hello = "Bem vindo ao acesso do usuário"
print("-=-= {} =-=-".format(hello))
print("-="*20)
print("O que você deseja fazer:"
      "\n[ LOGIN ]"
      "\n[ SING IN ]")
escolha = input("Qual a sua escolha: ").upper()


def obtendo_dados():
    nome = input("Informe o seu nome completo: ")
    idade = input("Informe a sua idade: ")
    genero = input("Informe o seu gênero: ")
    cpf = input("Informe o número do seu cpf: ")
    endereco = input("Informe seu endereço: ")
    telefone = input("Informe o seu telefone: ")
    email = input("Informe o seu Email: ")
    senha = input("Informe uma senha: ")

    return {
        "nome": nome,
        "idade": idade,
        "genero": genero,
        "cpf": cpf,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "senha": senha
    }


usuarios = [{"nome": "João marculino", "idade": 43, "genero": "Masculino", "cpf": "435.238.944-33", "endereco": "Jardim Tulipas, São Gonçalo", "telefone": "(11) 93824-6598", "email": "Marculino@outlook.com", "senha": "Marculino@Gostosao"}]

if escolha == "LOGIN":
    print("Informe o seu Email e a sua Senha.")
    eMail = input("Email: ")
    sEnha = input("Senha: ")

    login_valido = False
    for usuario in usuarios:
        if usuario["email"] == eMail and usuario["senha"] == sEnha:
            login_valido = True
            break
    if login_valido:
        print("Login Bem-Sucedido!")
    else:
        print("Email ou senha incorretos!")
else:
    SING_IN = True
    while SING_IN:
        cadastro_usuario = obtendo_dados()
        usuarios.append(cadastro_usuario)

        resposta = input("Deseja cadastras mais um usuário? (S / N): ")
        if resposta.upper() != "S":
            SING_IN = False

print(usuarios)
