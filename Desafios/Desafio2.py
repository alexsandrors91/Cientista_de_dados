##Esse bimestre na faculdade você precisa tirar nota 8 de média para
#passar na matéria, desenvolva um script que leia a nota de suas
# 3 provas, tire a média delas e verifique se você passou.

nota_1 = float(input('Digite a nota da primeira prova: '))
nota_2 = float(input('Digite a nota da segunda prova: '))
nota_3 = float(input('Digite a nota da terceira prova: '))

media = (nota_1 + nota_2 + nota_3)/3

if media < 8:
    print('Reprovado')
else:
    print('Aprovado')