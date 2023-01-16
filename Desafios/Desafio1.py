#Seu primeiro desafio é desenvolver um programa para um depósito de
#bebidas que valide venda de bebidas para maiores de idade (maior ou
#igual 18 anos) no mercado, o programa deve receber do usuário os
#valores do nome e ano que ele nasceu e retornar se ele pode comprar
#bebidas.

u_nome = input('Digite o nome do cliente: ')
u_ano  = int(input('Digite o ano de nascimento do cliente: '))

idade =  2018 - u_ano 
print(u_nome)
if idade >= 18:
    print('Ele pode comprar bebida!')
else:
    print('Menor não pode comprar bebida') 
