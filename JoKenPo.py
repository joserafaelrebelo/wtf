def endMenu():
    print('Escolher modo de jogo (PRESS 1)')
    print('Jogar novamente no modo atual (PRESS 2)')
    print('Encerrar programa (PRESS 0)')
    escolha = int(input('>>Digite aqui : '))

    if escolha == 1 :
        menu()
    elif escolha == 2 :
        vsCpu()
    elif escolha == 0 :
        print ('Encerrando o jogo')
        sleep(2)
        print("Jogo encerrado. \nObrigado por jogar.")
        0
    else :
        print ('Escolha invalida')
        print ('TENTE NOVAMENTE')
        endMenu()
def vsCPU():
    print('It\'s JO-KEN-PO Time!!\nNa sua vez escolha entre Pedra, Papel e Tesoura.')

    Pedra = str('Pedra')
    Papel = str('Papel')
    Tesoura = str('Tesoura')

    Jogador1 = input('Sua vez :')
    Jogador2 = random.choice([Pedra,Papel,Tesoura])

    print ('CPU jogou : ' , Jogador2)



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

    endMenu()

    
