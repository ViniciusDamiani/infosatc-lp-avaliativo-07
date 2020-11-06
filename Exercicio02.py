#Faça um programa que solicite dois números ao usuário e exiba a multiplicação deles. 
digito1=int(input("Insira um número: "))
digito2=int(input("Insira outro número: "))

multDigitos=(lambda x: digito1*digito2)
print(multDigitos(0))
