# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

print("{:=^40}".format(" ETERNO LOJA "))

compra = float(input("Digite o valor da compra: R$ "))

print("""Selecione a forma de pagamento:
      [1] À vista dinheiro: 10% de desconto
      [2] À vista cartão: 5% de desconto
      [3] Em até 2x no cartão: preço normal
      [4] 3x ou mais no cartão: 20% de juros""")

tpagamento = int(input("Selecione a opção de pagamento: "))

if tpagamento == 1:
    total = compra - (compra * 10 / 100)
    print("Sua compra era R${:.2f}, com 10% de desconto fica R${:.2f}.".format(compra, total))

elif tpagamento == 2:
    total = compra - (compra * 5 / 100)
    print("Sua compra era R${:.2f}, com 5% de desconto fica R${:.2f}.".format(compra, total))

elif tpagamento == 3:
    total = compra
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f} sem juros.".format(parcela))

elif tpagamento == 4:
    qtparcelas = int(input("Quantas vezes no cartão? "))
    total = compra + (compra * 20 / 100)
    vlparcela = total / qtparcelas
    print("Sua compra será parcelada em {}x de R${:.2f} com juros.".format(qtparcelas, vlparcela))

else:
    total = compra  # Para evitar erro no print final
    print("Opção inválida. Tente novamente.")

print("Sua compra de R${:.2f} terá o valor final de R${:.2f}.".format(compra, total))
