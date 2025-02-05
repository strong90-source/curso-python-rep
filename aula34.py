'''
Repeticoes
while(enquanto)
Executa uma acao enquanto uma condicao for verdadeira
'''
condicao = True

while condicao:
    nome = input('Qual o seu nome ?')
    print(f'Seu nome {nome}')

    if nome == 'sair':
        break

print('Acabou!!!')