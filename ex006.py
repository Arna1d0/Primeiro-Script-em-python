n1 = int(input('Digite um numero :'))
r2 = n1 * 2
r3 = n1 * 3
r4 = n1 ** (1/2)
        # outro jeito de fazer porcentagem e ** (1/2)=quadrada
        # \n e uma quebra de linha
        # {:.2f} isso é formatar o resultado pra duas casas depois da virgula ou seja duas casas
        # Outro jeito de fazeer é:
        # Print('O dobro de{} valeu {}.'.format(n, (n * 2)))
        # Print('O triple de {} vale {}, \n A raiz quadrada de {} é igual a {:,2f}.'.format(n, (1/2)))

print('O numero é {}. \n Seu dobro é {}. \n Seu triplo é {}. \n Sua raiza quadrada é {:.2f}.'.format(n1, r2, r3, r4))
