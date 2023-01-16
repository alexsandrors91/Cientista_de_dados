""""" 4 - Utilizando as informações abaixo, calcule a função f(x,y,z) para estas 3 variáveis.

$x = 2$

$y = 0.5$

$z = 12$

$f(x,y,z) = \frac{x^2-z}{yz}+xyz$
"""""
x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de y: '))
z = float(input('Digite o valor de z: '))

funcao = ((x** - z)/(y*z))+(x*y*z)
print(f'A função retorna {funcao:.2f}')