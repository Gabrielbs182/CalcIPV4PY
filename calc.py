def dec2bin(a): #Função que converte o índiced de números inteiros da lista em binário
  i = 0
  result = ''
  lista = []  
  #-------------------- Inicio do processo ---------------------#  
  while a>1:
    i = a%2
    lista.append (i)
    a = a//2
  if a == 1:
    lista.append (1)
  #-------------------- Fim do processo -------------------------# 
  while (len(lista))<8: #Preenche o octeto com zeros a esquerda
    lista.append(0)
  lista.reverse() #Reverte a lista
  for b in lista:  #transformando a lista em uma string
    result += str(b)
  return result

#---------------------------------------------------------------------

def bin2dec(n): #Função que converte um número decimal em binário
  
  result = ""
  i,dec = 0,0
  lista = n
  lista = list(lista)
  lista.reverse()
  #-------------------- Inicio do processo ---------------------#
  for x in (lista):
    if x == "1":
      dec += 2**i
    i += 1
  #-------------------- Fim do processo -------------------------#
  result = str(dec)
  return result

#----------------------------------------------------------------------
  
def end(masc,ip): #Função que calcula o endereço da sub-rede e disponibiliza tanto em binário quanto decimal.
  endereco,resultado = "",""
  listamasc,listaip = [],[]
  for x in masc:
    listamasc.append(x)
  for y in ip:
    listaip.append(y)
  for z in range (len(listamasc)):    
    if listamasc[z] == "0":
      listaip[z] = "0"
  for b in listaip:  #Transformando a lista em uma string
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

def separar(n): #Transforma uma string em lista de números inteiros.
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
def coletar(n,lista): #Função que coleta a entrada e devolve em binário string
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
def verificar(i,lista): #Recebe um número e verifica se o numero é valido
  teste,b = 0,0 #da valor inicial as variaveis
  if (len(lista)) != 4: #Verifica se tem a quantidade certa de vértices
    b = 1
  else:
    for x in range (len(lista)): #inicia um loop de acordo com o len
      if lista[x] < 0 or lista[x] > 255: #Condicional que verifica um valor mánimo e um valor máximo para a entrada
        b = 1
      else:
        b = 0
  return b #Retorna o valor de (b), se o valor de (b) for = 1 então ele informa que (i) não é uma informação valida, se (b) for = 0, então ele informa que é valida
