salario = float(input('Digite seu salario: R$'))
novo = salario + (salario * 15 / 100)
# Prestar atenção SEMPRE SE ESTA TIRANDO OU SOMANDO
print('Seu salario é {:.2f} com o aumento de 15% sera {:.2f}'.format(salario, novo))
