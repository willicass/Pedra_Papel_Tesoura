from time import sleep
from random import shuffle


def contar():
    print(f'\n{branco}3')
    sleep(1)
    print(f'{branco}2')
    sleep(1)
    print(f'{branco}1\n')
    sleep(1)


# Difinições de cores e estilos
azul = '\033[1;34m'
verde = '\033[1;32m'
branco = '\033[1;97m'
ciano = '\033[1;96m'
amarelo = '\033[1;93m'
vermelho = '\033[1;31m'
vermelhoclaro = '\033[1;91m'
cinza = '\033[1;37m'
negrito = '\033[;1m'
terminodecor = '\033[m'
linha = f'{negrito}~~' * 9
linhamaior = f'{negrito}~~' * 12


# Variáveis para executar funções
pontosjogador = 0
pontosmaquina = 0
continuarjogar = 'SIM'


print(linha)
print(f'{azul}BORA JOGAR JOKENPÔ')
print(linha)
sleep(1.5)
print(f'{azul}Faça sua{terminodecor}{cinza}{negrito} ESCOLHA')
print('')

while continuarjogar == 'SIM':
    opcoesmaquina = ["0", "1", "2"]
    shuffle(opcoesmaquina)
    jogadamaquina = opcoesmaquina[2]
    jogadaplayer = int(input(f'{verde}[0] - PEDRA\n'
                             f'{amarelo}[1] - PAPEL\n'
                             f'{ciano}[2] - TESOURA\n'
                             f'{azul}[3] - Mostrar resultado\n'
                             f'{vermelhoclaro}[4] - Parar de jogar\n\n'
                             f'{negrito}Digite a opção desejada: '))

    if jogadaplayer == 0:
        contar()
        if jogadamaquina == '2':
            print(linhamaior)
            print(f'{verde}PARABÉNS, VOCÊ VENCEU!!')
            print(linhamaior)
            pontosjogador += 1
            print(f'{verde}PEDRA{terminodecor} {negrito}X{terminodecor} {ciano}TESOURA')
            print(linhamaior)
            continuarjogar = str(input('Digite sim para continuar a jogar: ')).upper()
            print('')

        elif jogadamaquina == '1':
            print(linha)
            print(f'{vermelho}   VOCÊ PERDEU!!{terminodecor}')
            print(linha)
            pontosmaquina += 1
            print(f'{verde}PEDRA{terminodecor} {negrito}X{terminodecor} {amarelo}PAPEL')
            print(linha)
            continuarjogar = str(input('Digite sim para continuar a jogar: ')).upper()
            print('')

        else:
            print(linha)
            print(f'    {amarelo}EMPATOU!!')
            print(linha)
            print(f'{verde}PEDRA{terminodecor} {negrito}X{terminodecor} {verde}PEDRA')
            print(linha)
            continuarjogar = str(input('Digite sim para continuar a jogar: ')).upper()
            print('')

    elif jogadaplayer == 1:
        contar()
        if jogadamaquina == '0':
            print(linhamaior)
            print(f'{verde}PARABÉNS, VOCÊ VENCEU!!')
            print(linhamaior)
            pontosjogador += 1
            print(f'{amarelo}PAPEL{terminodecor} {negrito}X{terminodecor} {verde}PEDRA')
            print(linhamaior)
            continuarjogar = str(input('Digite sim para continuar a jogar: ')).upper()
            print('')

        elif jogadamaquina == '2':
            print(linha)
            print(f'{vermelho}   VOCÊ PERDEU!!{terminodecor}')
            print(linha)
            pontosmaquina += 1
            print(f'{amarelo}PAPEL{terminodecor} {negrito}X{terminodecor} {ciano}TESOURA')
            print(linha)
            continuarjogar = str(input('Digite sim para continuar a jogar: ')).upper()
            print('')

        else:
            print(linha)
            print(f'    {amarelo}EMPATOU!!')
            print(linha)
            print(f'{amarelo}PAPEL{terminodecor} {negrito}X{terminodecor} {amarelo}PAPEL')
            print(linha)
            continuarjogar = str(input('Digite sim para continuar a jogar: ')).upper()
            print('')

    elif jogadaplayer == 2:
        contar()
        if jogadamaquina == '1':
            print(linhamaior)
            print(f'{verde}PARABÉNS, VOCÊ VENCEU!!')
            print(linhamaior)
            pontosjogador += 1
            print(f'{ciano}TESOURA{terminodecor} {negrito}X{terminodecor} {amarelo}PAPEL')
            print(linhamaior)
            continuarjogar = str(input('Digite sim para continuar a jogar: ')).upper()
            print('')

        elif jogadamaquina == '0':
            print(linha)
            print(f'{vermelho}   VOCÊ PERDEU!!{terminodecor}')
            print(linha)
            pontosmaquina += 1
            print(f'{ciano}TESOURA{terminodecor} {negrito}X{terminodecor} {verde}PEDRA')
            print(linha)
            continuarjogar = str(input('Digite sim para continuar a jogar: ')).upper()
            print('')

        else:
            print(linha)
            print(f'     {amarelo}EMPATOU!!')
            print(linha)
            print(f'{ciano}TESOURA{terminodecor} {negrito}X{terminodecor} {ciano}TESOURA')
            print(linha)
            continuarjogar = str(input('Digite sim para continuar a jogar: ')).upper()
            print('')

    elif jogadaplayer == 3:
        if pontosjogador > pontosmaquina:
            print(linhamaior)
            print(f'Você está {verde}GANHANDO{terminodecor} com {verde}{pontosjogador}{terminodecor} '
                  f'e a máquina {vermelho}{pontosmaquina}')
            print(linhamaior + '\n')

        elif pontosjogador == pontosmaquina:
            print(linhamaior)
            print(f'Está {amarelo}EMPATADO{terminodecor}, você com {verde}{pontosjogador}{terminodecor} '
                  f'e a máquina {vermelho}{pontosmaquina}')
            print(linhamaior + '\n')

        else:
            print(linhamaior)
            print(f'Você está {vermelho}PERDENDO{terminodecor} com {verde}{pontosjogador}{terminodecor} '
                  f'e a máquina {vermelho}{pontosmaquina}')
            print(linhamaior + '\n')

    elif jogadaplayer == 4:
        if pontosjogador > pontosmaquina:
            print(linhamaior)
            print(f'Você {verde}GANHOU{terminodecor} com {verde}{pontosjogador}{terminodecor} '
                  f'e a máquina {vermelho}{pontosmaquina}')
            print(linhamaior + '\n')
            
        elif pontosjogador == pontosmaquina:
            print(linhamaior)
            print(f'Você{amarelo}EMPATATOU{terminodecor} com {verde}{pontosjogador}{terminodecor} '
                  f'e a máquina {vermelho}{pontosmaquina}')
            print(linhamaior + '\n')

        else:
            print(linhamaior)
            print(f'Você {vermelho}PERDEU{terminodecor} com {verde}{pontosjogador}{terminodecor} '
                  f'e a máquina {vermelho}{pontosmaquina}')
            print(linhamaior + '\n')
        quit()

    else:
        print(f'{vermelho}Valor digitado inválido!')
        continuarjogar = str(input(f'{negrito}Gostaria de tentar novamente? '))
