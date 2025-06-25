km = float(input('Digite a quantidade de km rodados: '))
dias = int(input('Digite os dias de utilização: '))
pago = (dias * 60) + (km * 0.15)


print ('O total a pagar é {:.2f}'.format(pago))
