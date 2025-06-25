n = str(input("Digite seu nome:")) .upper() .strip() #metodo upper para deixar as letras caixa alta, e metoto strip para tira espaços vaios 
nome = n.split()#Split para separar as frases 
print("Muito prazer em conhecer voce")
print("Seu primeiro nome {}".format(nome[0]))
print("seu ultimo nome é {}" .format(nome[len(nome)-1]))