nome = str(input("Digite seu nome:")).upper() .strip()
print("A letra A aparece {} na frase".format(nome.count("A")))
print("Aprimeira posisão da letra A é {}" .format(nome.find("A")+1))
print("A última posição da letra a é {}" .format(nome.rfind("A")+1))