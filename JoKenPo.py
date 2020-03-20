#JokenPo

print('It\'s JO-KEN-PO Time!!\nNa sua vez escolha entre Pedra, Papel e Tesoura.')

Jogador1 = input('Vez do Jogador nº1:')
Jogador2 = input('Vez do Jogador nº2:')
Pedra = str('Pedra')
Papel = str('Papel')
Tesoura = str('Tesoura')


if (Jogador1 == Jogador2):
    print('DRAW! Opa, temos um empate.Tente novamente!')

if (Jogador1 == Pedra  and Jogador2 == Tesoura):
    print('WE HAVE A WINNER! Parabéns ao Jogador nº1 pela vitória!!')
if (Jogador1 == Papel  and Jogador2 == Pedra):
    print('WE HAVE A WINNER! Parabéns ao Jogador nº1 pela vitória!!')
if (Jogador1 == Tesoura  and Jogador2 == Papel):
    print('WE HAVE A WINNER! Parabéns ao Jogador nº1 pela vitória!!')
else:
    print('WE HAVE A WINNER! Parabéns ao Jogador nº2 pela vitória!!')
