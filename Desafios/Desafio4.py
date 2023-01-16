#Faça um script que você coloque a quantidade de dias e descubra em qual trimestre esse dia está no ano.
n_dias = int(input('Digite o numero de dias: '))
dias_ano = 365
if n_dias <= 92:
    print('Voce esta no primeiro trimestre!')
elif n_dias > 92 and n_dias <= 183:
    print('Voce esta no segundo trimestre!')
elif n_dias > 183 and n_dias <= 275:
    print('Voce esta no terceiro trimestre!')
else: 
    print('Voce esta no quarto trimestre!')