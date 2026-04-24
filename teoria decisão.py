# Nesse código, analisaremos a idade do usuário e falaremos
# se é maior de idade ou não 
nome= input("digite o seu nome:")
idade= int(input("digite a sua idade"))

print("olá, ",nome,"! A sua idade é ",idade)

# A estrutura de decisão analisa uma comparação e executa o código
# com base na resoista. para itilizarmoos a estrutura de decisão, precisamos

# de comparadores, que são 
# - > maior
# - <menor
# - == igual
# - != diferente 
# - >= maior ou igual
# - <= menor ou igual
# - ! não

# O comando de decisão é o if
# A sintaxe é:
#if comparação
# E os itens a serem executados devem estar em um bloco identado
# if 20 > 30
#   print ("algo de errado não está certo")

if idade >= 18:
    print("você é maior de idade")
    print("você já pode ter carteira de motorista")
else:
    print("você é menor de idade")
    print("Não pode dirigir ainda")
    