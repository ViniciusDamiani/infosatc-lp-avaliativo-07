#Faça um programa que solicite dez números ao usuário, depois disso, exiba todos números pares e só
#então exiba todos os números ímpares. Utilize a função filter para fazer isso.
armazenaDigitos=[]
numPares=0
numImpares=0
def linhas():
    print("-"*35)

for x in range(10):
    digitos=int(input("Digite um numero: "))
    armazenaDigitos.append(digitos)
pares = filter(lambda valor: valor % 2 == 0, armazenaDigitos)

for valor in pares:
    print("Esses são os números Pares "+str (valor))
linhas()

impares = filter(lambda valor: valor % 2 != 0, armazenaDigitos)
for valor in impares:
    print("Esses são os números Ímpares "+str(valor))


