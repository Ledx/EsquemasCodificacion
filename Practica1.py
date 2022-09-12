import sys

def binAdec(numero_binario):
    numero_decimal = 0

    for posicion, digito_string in enumerate(numero_binario[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion

    return numero_decimal

def existenciaClanes(G,K):
    respuesta = []
    clanes = []
    respuesta.append("Si")
    clanes.append(" ")
    clanes.append(" ")
    respuesta.append(clanes)
    return respuesta

#entrada = sys.argv[1]
entrada = "e3.txt"
ejemplarRAW = open(entrada,"r")
cadena = ejemplarRAW.read()
ejemplarRAW.close()
contadorParam = 1
vertices = []
aristas = []
matriz = []
matrizDup = []
G = []
for c in cadena:
    if c != "1":
        contadorParam += 1
    else:
        break
matrizStr = cadena[0:contadorParam*contadorParam*2]
kStr = cadena[contadorParam*contadorParam*2:len(cadena)]

for i in range (1,contadorParam+1):
    vertices.append(i)
a = 0
b = contadorParam*2
for j in range (0,contadorParam):
    matriz.append(list(matrizStr[a:b][-contadorParam:]))
    matrizDup.append(list(matrizStr[a:b][-contadorParam:]))
    a = b
    b += 2*contadorParam


for i in range (0,contadorParam):
    for j in range(0, contadorParam):
        matrizDup[i][j] = 0

for i in range (0,contadorParam):
    for j in range(0, contadorParam):
        if int(matriz[i][j]) != 0 and matrizDup[i][j] == 0:
            aristas.append(str(i+1)+'-'+str(j+1))
            matrizDup[i][j] = 1
            matrizDup[j][i] = 1

K = binAdec(kStr[contadorParam:-contadorParam])
G.append(vertices)
G.append(aristas)
G.append(matriz)
G.append(K)
print(aristas)
print("El número de vértices de G es: ",len(vertices))
print("El número de aristas de G es: ",len(aristas))
print("El valor de K es: ", K)
print("La codificación del primer vértice de G es: ",vertices[0])
print("La codificación de la primera arista de G es: ",aristas[0])
if K > 2:
    print("Lo sentimos, no se tiene resuelto el problema para k > 2")
else:
    respuesta = existenciaClanes(G, K)
    print("¿Existe una partición de G tal que se forman dos clanes? ",respuesta[0])
    if respuesta[0] == "Si":
        print("Clan 1 es: ",respuesta[1][0])
        print("Clan 2 es: ",respuesta[1][1])