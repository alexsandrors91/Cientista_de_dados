"""""3 - Crie um algoritmo simples que calcule se o número inserido é multiplo
 de 2 e 3 ao mesmo tempo. (O número deve ser sempre inteiro)"""""
num = int(input('Digite o numero: '))
se_par_imp = num%2
if se_par_imp == 0:
    print(f'O numero {num} digitado é multiplo de 2.')
else:
    print(f'O numero {num} digitado é multiplo 3. ')