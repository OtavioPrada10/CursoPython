"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome  = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if (nome and idade):
    print('Seu nome é ', nome) 
    quantidadeLetras = len(nome)
    print('Seu nome invertido é', nome[::-1])

    if(' ' in nome ):
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print('A primeira letra dos eu nome é ', nome[0])
    print(f'A ultima letra do seu nome é {nome[-1]}' )
else:
    print('Informações não foram digitadas corretamente!!!!')