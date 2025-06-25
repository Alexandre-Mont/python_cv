#medir a área e a quantidade de tintas 
alt = float(input('Digite a altuta h: '))
lar = float(input('digite a Largura L: '))
#Calcula área
print('Área da parse e {:.2f} m²'.format(alt*lar))

#quantidade de tinta necessária 
area = alt * lar
tinta = area / 2
print('Tinta necessária {:.f} l'.format(tinta))


