#Faça um programa que solicite cinco números ao usuário, depois disso, exiba apenas os números
#maiores do que 10. Utilize a função filter para fazer isso.
armazenaDigitos=[]
for x in range(5):
    digitos=int(input("Digite um numero: "))
    armazenaDigitos.append(digitos)
z = list(filter(lambda x: x >=10, armazenaDigitos))
print(z)

