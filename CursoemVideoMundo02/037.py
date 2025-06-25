#Corversor de base
nun = int(input("selecione numero inteiro: """))
print("""Escola uma sdas bazes para conversão
      [1] converter BINÀRIO
      [2] convertere OCTAL
      [3] converter HEXADECIMAL""")
opcao = int(input("Qual a sua opção:"))

if opcao == 1:
    print("{} convertido em BIN é {} ".format(nun, bin(nun)[2:])) 
#[2:] serve para fazer o fatiamento de informações esta excluindo os dois primors digitos
elif opcao == 2:
    print("{} convertido em otal é {} ".format(nun, oct(nun)[2:]))
elif opcao == 3:
    print("{} onvertido a hexa é {} ".format(nun, hex(nun)[2:]))
else:
    print("selecione um numero válido")
