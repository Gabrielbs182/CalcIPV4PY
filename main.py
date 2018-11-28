from calc import * #Importo todas as funções de calc.py

teste,b = 0,0 #Valor inicial das variáveis de controle
i = str(input("\nInforme o numero do IPV4: "))
#--------------- Inicio da verificação de validade da entrada ------#
while teste != 1:
  lista = separar(i) #Recebe o ip como lista de inteiros
  j = verificar(i,lista) #Verifica se a variável (i) atende os limites
  if j == 1: #A variavel (j) é o retorno da função verificar(), se b for 1 é porque (i) está invalida nesse caso o programa aciona a condicional
    print("\nInformação invalida")
    i = str(input("\nInforme o numero do IPV4 Novamente: "))
  else:
    teste = 1
    a = coletar(i,lista) #A variável (a) recebe o número do ipv4 em binário
#--------------- Fim da verificação de válidade da entrada --------#
teste,j = 0,0 #Reinicia os valores das variáveis de controle

m = str(input("\nInforme o numero da Máscara de sub-rede: "))
#--------------- Inicio da verificação de validade da entrada ------#
while teste != 1:
  lista = separar(m)
  j = verificar(m,lista)
  if j == 1:
    print("\nInformação invalida")
    m = str(input("\nInforme o numero da Máscara de sub-rede: "))
  else:
    teste = 1
    b = coletar(m,lista) #A variável (b) recebe o número da mascara de sub-rede em binário
#--------------- Fim da verificação de válidade da entrada --------#

c,d = broad(b,a) #A variavel (c) tem como valor o broadcast em binario, a variavel (d) tem como valor o broadcast
f,g = end(b,a) #A variavel (f) tem como valor o Endereço da subrede em binario, a variavel (g) tem como valor o Endereço da subrede.

print('\nEndereço IP em binário: ',a)
print('\nMáscara de sub-rede em binário: ',b)
print("\nEndereço da sub-rede =",g)
print("\nEndereço de Broadcast =",d) 
print("\nEndereço da sub-rede em binário =",f)
print("\nEndereço de Broadcast em binário =",c)
