preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
# Para calcular a porcentagem e fazer vezes a porcentagem que vc deseja dividido por 100
# no caso de 15% coloca valor * 15 / por 100
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R%{:.2f}'.format(preço, novo))