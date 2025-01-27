"""
Formatacao basica de Strings
s - string
d- int
f - float
.<numero de digitos>f
x ou x - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Convertion flags - !r !s !a
"""

variavel = "ABC"
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{10000.48498499:,.2f}')

