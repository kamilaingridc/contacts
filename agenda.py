def message():
    print("Bem-vindo à sua Agenda de Contatos.")


def dictionary():
    contacts = {
        "Fulana": {
            "Sobrenome": "Silva",
            "Celular": 11912345678,
            "E-mails": [
                "fulana1@mail.com",
                "1fulana@mail.com"],
            "Endereço": "Rua das Flores, 123, Bairro Felicidade, Cidade Alegre, Estado Feliz, CEP: 12345-678",
            "Aniversário": "10/02/1985"
        },
        "Beltrana": {
            "Sobrenome": "Carvalho",
            "Celular": 71432109876,
            "E-mails": [
                "beltrana1@mail.com",
                "1beltrana@mail.com"],
            "Endereço": "Travessa das Estrelas, 1213, Bairro Amor, Cidade Celestial, Estado Divino, CEP: 45678-901",
            "Aniversário": "15/07/1990"
        },
        "Ciclana": {
            "Sobrenome": "Mendes",
            "Celular": 52543210987,
            "E-mails": [
                "ciclana@mail.com",
                "1ciclana@mail.com"],
            "Endereço": "Alameda dos Sonhos, 1011, Bairro Harmonia, Cidade Tranquila, Estado Plácido, CEP: 34567-890",
            "Aniversário": "30/02/1998"
        }
    }
    return contacts


def criarTXT(contacts):
    with open('agenda.txt', 'w', encoding="utf-8") as arquivo:
        for nome, contato in contacts.items():
            arquivo.write(f"{nome}: {contato}\n")


def cadastrar(contacts):
    nome = input("Digite o nome para cadastrar: ")
    sobrenome = input("Digite o sobrenome: ")
    celular = int(input("Digite o número de celular: "))
    emails = input("Digite os e-mails separados por vírgula: ").split(',')
    endereco = input("Digite o endereço completo: ")
    aniversario = input("Digite a data de aniversário (DD/MM/AAAA): ")

    novo_contato = {
        "Sobrenome": sobrenome,
        "Celular": celular,
        "E-mails": emails,
        "Endereço": endereco,
        "Aniversário": aniversario
    }

    contacts[nome] = novo_contato
    print(f"{nome} foi cadastrado com sucesso!\n")
    criarTXT(contacts)


def remover(contacts):
    nome = input("Digite o nome para remover: ")
    if nome in contacts:
        del contacts[nome]
        print(f"Contato '{nome}' removido com sucesso.\n")
        criarTXT(contacts)
    else:
        print(f"O contato '{nome}' não foi encontrado na agenda.\n")


def mostrar_contato(contacts):
    nome = input("Digite o nome do contato para exibir seus dados: ")
    if nome in contacts:
        print(f"Dados de {nome}:")
        for key, value in contacts[nome].items():
            print(f"{key}: {value}")
    else:
        print(f"O contato '{nome}' não foi encontrado na agenda.")


def choice():
    return int(input('Escolha uma das opções abaixo:\n'
                     '[1] Contatos | [2] Cadastrar Novo Contato | [3] Remover Contato\n'
                     '[4] Mostrar Dados de um Contato | [5] Sair\n'))


def switch(option, contacts):
    if option == 1:
        print("Contatos:")
        for contact in contacts:
            print(contact)
    elif option == 2:
        cadastrar(contacts)
    elif option == 3:
        remover(contacts)
    elif option == 4:
        mostrar_contato(contacts)
    elif option == 5:
        criarTXT(contacts)
        print("Agenda salva no arquivo 'agenda.txt'.")
        exit()


if __name__ == '__main__':
    contacts = dictionary()
    while True:
        try:
            message()
            choice_input = choice()
            switch(choice_input, contacts)
        except ValueError:
            print("Dado inválido. Tente novamente!")
