import pandas as pd
#Crianando uma lista de valores

date = [10,20,30,40,50] #Lista é []
#Criando uma séria apartir da lista
serie1 = pd.Series(date)

print(serie1)

exemplo02 = {"A":100, "B":200, "C":300, "D":400, "E":500}
serie2 = pd.Series(exemplo02)
print(serie2)
 
print("x"*50)

#Cria lista baseada em um dicionário 
dados = {
    "Nome":["Alexandre","Yan","Josy","Yago", "Yohanna", "Yoha"],
    "Idade":[46,11,46,11,22,25]
}

#cria seria apartir do dicionáriio
serie_idade = pd.Series(dados["Idade"],index=dados["Nome"])
print("Série de idades")
print(serie_idade)

media = serie_idade.mean()

print("\nIdade média {:.3f}".format(media))
