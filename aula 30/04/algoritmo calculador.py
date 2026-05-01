print ("|-----------------------------|")
print ("|      CALCULADORA            |")
print ("|-----------------------------|")
print()
print("essa calculadora, faz todas as operações")
print("a partir de dois numeros que você informar")
print()

print("digite o valor correspondente a operação que deseja realizar:")
print()
print("1 - as 4 operações")
print("2 - média de 3 valores")
print("3 - formula de bhaskara")
print()

opção = int(input("digite a opção desejada: "))

match opção:
    case 1:
        num1 = float(input("digite o primeiro numero: "))
        num2 = float(input("digite o segundo numero: "))

        adição = num1 + num2
        print(f"o resultado da adição é: {adição}")

        subtração = num1 - num2
        print(f"o resultado da subtração é: {subtração}")

        multiplicação = num1 * num2
        print(f"o resultado da multiplicação é: {multiplicação}")

        # verificando divisão por zero
        if num2 != 0:
            divisão = num1 / num2
            print(f"o resultado da divisão é: {divisão}")
        else:
            print("não é possível dividir por zero")
    case 2:
        num1 = float(input("Digite seu primeira numero: "))
        num2 = float(input("Digite seu segundo numero: "))
        num3 = float(input("Digite seu terceiro numero: "))

        media = (num1 + num2 + num3) / 3
        print(f"o resultado da média é: {media}")

    case 3:
        print("formula de bhaskara")