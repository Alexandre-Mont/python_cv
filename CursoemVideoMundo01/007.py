# Calcula a média do alunos 
aluno01 = input('Digite o nome do aluno: ')

# Lista para armazenar as notas do aluno
notas_01 = []
for c in range(4):  # range define a quantidade de iterações
    notas_01.append(float(input(f'Insira a {c + 1}ª nota do: ')))  # .append faz a inserção

# Função para calcular média
def calcula_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Função lambda para arredondar média
arredonda_media = lambda media: round(media, 2)

# Calcula média
media = calcula_media(notas_01)
media_arredondada = arredonda_media(media)

# Faz validação de aprovação
situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

# Imprime o resultado
print('Estudante:', aluno01)
print('Notas do estudante:', notas_01)
print('Média das notas:', media_arredondada)
print('Situação do aluno:', situacao)
