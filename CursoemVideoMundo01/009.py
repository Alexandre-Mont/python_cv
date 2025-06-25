n = int(input('Digite o número inteiro: '))
operacao = input('Digite a operação desejada (+, -, *, /): ')

print(f"\nTabuada do {n} usando a operação '{operacao}':")

if operacao == '+':
    for i in range(1, 11):
        print(f"{n} + {i} = {n + i}")
elif operacao == '-':
    for i in range(1, 11):
        print(f"{n} - {i} = {n - i}")
elif operacao == '*':
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")
elif operacao == '/':
    for i in range(1, 11):
        if i != 0:
            print(f"{n} / {i} = {n / i:.2f}")
        else:
            print("Divisão por zero não é permitida.")
else:
    print("Operação inválida. Escolha entre +, -, * ou /.")
'''print('{} x {} = {}'.format(n,1,n*1))
print('{} x {} = {}'.format(n,2,n*2))
'''