alt = float(input('Qual a altura da parede:'))
lar = float(input('Qual a largura da parede:'))
area = alt * lar
print('A sua parede tem {}X{} sendo assim a sua area é de {} metros para essa area sera necesasario {} litros de tinta '.format(alt, lar, area, (area / 2)))
#tinta = area / 2
#print('Para pinta essa area sera necessario {} litros de tinta.'.format(tinta))
#.format(alt, lar, area, (area / 2))) forma reduzida escrevendo a conta a ser feita direto no format ajudando e ser mais objetivo o codigo