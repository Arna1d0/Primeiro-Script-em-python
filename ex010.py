moeda = float(input('Quanto de dinheiro tem na carteira? R$ '))
print('Você tem R${:.2f}, com isso você comsegue comprar US${:.2f}.'.format(moeda, (moeda / 3.27)))
# os pontos flutuantes sao os pontos com virgula da erro