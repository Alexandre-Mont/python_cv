5#digite um numero e divida em unidade, dezena, sentenna em milhar

num = int(input('Digite um numero 0 à 9999  :'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Analizando seu número {}".format(num))
print("__"*50)
print("Undade {}" .format(u))
print("Dezena {}" .format(d))
print("Centena {}" .format(c))
print("Milhae {}" .format(m))
