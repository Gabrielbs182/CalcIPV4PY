def dec2bin(a): #calculadora que vai converter o indice da lista em binario.

  i = 0
  result = ''
  lista = []
  while a>1:
    i = a%2
    lista.append (i)
    a = a//2
  if a == 1:
    lista.append (1)
  while (len(lista))<8: #Deixar o numero sempre sendo um octeto de bit
    lista.append(0)
  lista.reverse()
  for b in lista:  #transformando a lista em uma string
    result += str(b)
  return result

#--------------------------------------------------------

def bin2dec(n): #Calculadora que transforma de binario para decimal
  
  result = ""
  i,dec = 0,0
  lista = n
  lista = list(lista)
  lista.reverse()
  for x in (lista):
    if x == "1":
      dec += 2**i
    i += 1
  result = str(dec)
  return result

  #------------------------------------------

def end(masc,ip): #Função que calcula o endereço da subrede e disponibiliza tanto em binario quanto decimal.
  endereco,resultado = "",""
  listamasc,listaip = [],[]
  for x in masc:
    listamasc.append(x)
  for y in ip:
    listaip.append(y)
  for z in range (len(listamasc)):    
    if listamasc[z] == "0":
      listaip[z] = "0"
  for b in listaip:  #transformando a lista em uma string
    endereco += str(b)
  lista = separar(endereco)
  for x in range (len(lista)):
    a = str(lista[x])
    result = bin2dec(a)
    if x != 3: #Essa condicional evita que seja concatenado junto a string um ponto extra no final
      resultado+=result+'.'
    else:
      resultado+=result

  return [endereco,resultado]

#---------------------------------------------------------

def broad(masc,ip):#Função que faz o mesmo porem calcula o broadcast.

  broadcast,resultado = "",""
  listamasc,listaip = [],[]
  for x in masc:
    listamasc.append(x)
  for y in ip:
    listaip.append(y)
  for z in range (len(listamasc)):
    if listamasc[z] == "0":
      listaip[z] = "1"
  for b in listaip:  #transformando a lista em uma string
    broadcast += str(b)
  lista = separar(broadcast)
  for x in range (len(lista)):
    a = str(lista[x])
    result = bin2dec(a)

    if x != 3: #Essa condicional evita que seja concatenado junto a string um ponto extra no final
      resultado+=result+'.'
    else:
      resultado+=result

  return [broadcast,resultado]

#--------------------------------------------

def separar(n): #Transforma uma string em lista de numeros inteiros.

  linha = ""
  lista = []
  n += "." 
  for x in n: 
    if x != ".": #usando o ponto para separar os vertices.
      linha += x
    else:
      mat = int(linha) #transformo o numero de str para int.
      lista.append(mat) #Adiciono a um vertice na lista em INT.
      linha = "" #reinicio o valor da 
  return lista

#------------------------------------------------------------------

def coletar(n,lista): #Faz a coleta dos dados e calcula.  

  resultado = ""
  for x in range (len(lista)):
    a = lista[x]
    result = dec2bin(a)
    if x != 3: #Essa condicional evita que seja concatenado junto a string um ponto extra no final
      resultado+=result+'.'
    else:
      resultado+=result
  return resultado

#---------------------------------------------

def ipv4(): #Recebe o numero do ip e passar pela função da coleta e verifica se o numero é valido.

  teste,b = 0,0 #da valor inicial as variaveis
  ip = "" #da valor inicial a string
  i = str(input("\nInforme o numero do IPV4: "))
  while teste != 1:
    lista = separar(i) #chama a função
    for x in range (len(lista)): #inicia um loop de acordo com o len
      if lista[x] < 0 or lista[x] > 255: #condicional
        teste = 0 #controle do loop
        b = 1 #controle da condicional a seguir
      else:
        teste = 1
    if b == 1: #condicional de informação invalida
      print("\nInformação invalida")
      i = str(input("\nInforme o numero do IPV4 Novamente: ")) #pede novamente o valor de i
      teste = 0
      b = 0
  ip = coletar(i,lista)
  return ip

#-------------------------------------------------------------#

def masc(): #Recebe o numero da mascara e passa pela função da coleta e verifica se o numero é valido.

  teste,b = 0,0 #valor inicial
  masc = "" #inicia o valor da string
  g = str(input("\nInforme o numero da Máscara de sub-rede: ")) #recebe o valor da mascara
  while teste != 1:
    lista = separar(g) #chama a função separar
    for x in range (len(lista)): #loop de acordo com o len
      if lista[x] < 0 or lista[x] > 255:
        teste = 0 #variavel de controle
        b = 1 #variavel de controle
      else:
        teste = 1
    if b == 1: #condicional que detecta informação invalida
      print("\nInformação invalida")
      g = str(input("\nInforme novamente o numero da Máscara de sub-rede:")) #pede novamente o valor da mascara.
      teste = 0
      b = 0
  masc = coletar(g,lista)
  return masc

#---------------------------------------------

def end(masc,ip): #Função que calcula o endereço da subrede e disponibiliza tanto em binario quanto decimal.
  endereco,resultado = "",""
  listamasc,listaip = [],[]
  for x in masc:
    listamasc.append(x)
  for y in ip:
    listaip.append(y)
  for z in range (len(listamasc)):    
    if listamasc[z] == "0":
      listaip[z] = "0"
  for b in listaip:  #transformando a lista em uma string
    endereco += str(b)
  lista = separar(endereco)
  for x in range (len(lista)):
    a = str(lista[x])
    result = bin2dec(a)
    if x != 3: #Essa condicional evita que seja concatenado junto a string um ponto extra no final
      resultado+=result+'.'
    else:
      resultado+=result

  return [endereco,resultado]

#---------------------------------------------------------

def broad(masc,ip): #Função que faz o mesmo porem calcula o broadcast.

  broadcast,resultado = "",""
  listamasc,listaip = [],[]
  for x in masc:
    listamasc.append(x)
  for y in ip:
    listaip.append(y)
  for z in range (len(listamasc)):
    if listamasc[z] == "0":
      listaip[z] = "1"
  for b in listaip:  #transformando a lista em uma string
    broadcast += str(b)
  lista = separar(broadcast)
  for x in range (len(lista)):
    a = str(lista[x])
    result = bin2dec(a)
    if x != 3: #Essa condicional evita que seja concatenado junto a string um ponto extra no final
      resultado+=result+'.'
    else:
      resultado+=result
  return [broadcast,resultado]