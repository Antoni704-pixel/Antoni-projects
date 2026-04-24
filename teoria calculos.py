nome = input("Digite o seu nome: ")
turma = input("Digite sua turma: ")

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("Olá, seu nome é", nome + "!")
print("Sua turma é", turma)
print("Sua média é", round(media, 2))

if media >= 7:
    print("Você passou")
    print("Parabéns")
elif media >= 4:
    print("Você está de recuperação")
else:
    print("Você reprovou")
    print("Que pena")