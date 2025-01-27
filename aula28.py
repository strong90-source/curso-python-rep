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

nome = input('Qual o teu nome? ')

idade = input('E a sua idade? ')

if nome and idade:
    print(f'Nome: {nome}')
    print(f'o teu nome invertido:  {nome[::-1]}')
    if " " in nome:
        print(f'O seu nome tem espacos!!!')
    if " " not in nome:
        print(f'O seu nome nao tem espacos!!! ')
    print(f'O seu nome tem: {len(nome)} letras')
    print(f'A primeira letra do seu nome: {nome[:1:1]}')
    print(f'A ultima letra do seu nome: {nome[-1::]}')
else:
    print('Desculpe mas certos campos tao vazios!!! ')