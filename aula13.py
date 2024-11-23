nome = 'Ricardo Martins'
altura = 1.73
peso = 89
imc = peso / altura ** 2

linha_1 = f'O meu nome: {nome} e tenho: {altura:.2f} de altura'
linha_2 = f'O meu indice de massa corporal: {imc:.2f}'

print(linha_1)
print(linha_2)

# O Índice de Massa Corporal (IMC) é uma fórmula que indica se uma pessoa está dentro de uma faixa de peso saudável. 
# Para calcular o IMC, basta dividir o peso (em kg) pela altura (em metros) ao quadrado: