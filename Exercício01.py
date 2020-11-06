#Faça um programa que solicite o nome do usuário e a idade do usuário, depois disso exiba a mensagem:
#“{nome} possui {idade} anos.”. 

nomeUsuario=str(input("Insira seu nome: "))
idadeUsuario=str(input("Insira sua idade: "))

armazenaDados=[lambda x: nomeUsuario, lambda x: idadeUsuario]
for x in armazenaDados:
    print(x(0))


























#print("Olá "+nome+", analisei aqui e você possui "+idade+" anos, certo?")
