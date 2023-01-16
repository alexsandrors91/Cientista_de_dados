#A fisioterapeuta que você vai gosta muito de brincar com números, e
#pediu para você criar um sistema que verifique se a altura inserida é
#par ou impar.

altura = float(input('Insira uma altura: '))
altura = altura*10
rest = float(altura%2)


if rest == 0:
    print('altura par!')
else:
    print('altura impar!')