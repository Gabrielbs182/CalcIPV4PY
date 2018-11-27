from calc import *

a = ipv4()
b = masc()
c,d = broad(b,a)
f,g = end(b,a)
print('\nEndereço IP em binário: ',a)
print('\nMáscara de sub-rede em binário: ',b)
print("\nBroadcast da subrede =",c)
print("\nBroadcast da subrede em binario é =",d)
print("\nEndereço da subrede =",g)
print("\nEndereço da subrede em binario é =",f)
