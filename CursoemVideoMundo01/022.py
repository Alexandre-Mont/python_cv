nome = str(input("Digite seu nome ")).strip() #retira os espaços em exesso da digitação

print("Análizando seu nome!")
print('Seu nome em maiusculo e {}'.format(nome.upper()))
print("seu no nome em minusculo e {}".format(nome.lower()))
print("seu nome em caixa alta a primeira letra {}".format(nome.capitalize()))
print("Seu nome com a Primeira letra em caixa alta {}".format(nome.title()))
print("seu nome tem {}  letras".format(len(nome)-nome.count(" ")))
print("Seu primeiro nome tem {}".format(nome.find(" ")))
print("_"*50)
separa = nome.split()
print("seu primeiro nome é {} e tem {} letras ".format(separa[0], len(separa[0])))
