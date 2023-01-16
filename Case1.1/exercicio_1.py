"""""1 - Peça ao usuário para inserir o valor da compra e em 
seguida em quantas vezes ele quer parcelar a compra. Ao final, 
imprima essas informações e o valor de cada parcela."""""

def Compra():
    valor = float(input('Digite o valor total da compra: '))
    num_parcelas = int(input('Digite em quantas vezes quer parcelar: '))
    valor_final = valor/num_parcelas
    print(f'O valor da compra foi {valor} e voce parcelou em {num_parcelas} o valor da parcela é {valor_final:.2f}')

Compra()

