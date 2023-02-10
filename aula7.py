n1 = int(input('Digite um valor :'))
n2 = int(input('Digite outra valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {} \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end='')
print('Divisão inteira é {} e potência {}'.format(di, e))

# para quebrar a linha \n e para nao quebrar a linha e , end=''