primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(f"O primeiro_valor='{primeiro_valor}' e maior ou igual que o segundo_valor='{segundo_valor}'" )

elif primeiro_valor <= segundo_valor:
    print(f"O segundo_valor='{segundo_valor}' e maior ou igual que o primeiro_valor='{primeiro_valor}'" )

else:
    print('Nao consegui calcular nada!!! Volte mais tarde')