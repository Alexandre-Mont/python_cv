velocidade = float(input("Qual a velocidade atual do caro "))
if velocidade > 80:
    print("Você foi multado excedeu o lomite de velociadde de 80km/h")
    multa = (velocidade-80) * 7
    print("Você foi multado, deve R${:.2f} pelo excesso de velocidade".format(multa))
else:
    print("siga e tenha um bpm dia")