#Desenvolva um sistema que leia 3 números e diga qual é o maior (se houver empate, exiba os empatados).
n1 = int(input('Digite o primeiro num: '))
n2 = int(input('Digite o segundo num: '))
n3 = int(input('Digite o terceiro num: '))

if n1 > n2 and n1> n3:
    print('O primeiro é maior {}'.format(n1))

elif n2 > n1 and n2 > n3:
   print('O segundo é maior {}'.format(n2))

elif n3 > n1 and n3 > n2:
    print('O Terceiro é maior {}'.format(n3))

else:
    print(n1,n2,n3)