import random

#recebe a quantidade de vezes que o dado foi rodado
#devolve um lista contendo os dados rolados.

def rolar_dados(quant):
    lista = []
    i = 0
    while i < quant:
        sorteio = random.randint(1,6)
        lista.append(sorteio)
        i = i + 1
    return lista

#recebe: uma lista de dados rolados, uma lista de dados já guardados e um número inteiro representado o índice do dado a ser armazenado
#retorna: uma lista com dois valores, o primeiro valor representando a lista de dados rolados e o segundo representando a lista de dados armazenados no estoque

def guardar_dado(rolados,guardados,indice):
    lista_final = []
    novo_guardados = []

    i = 0
    while i < len(guardados):
        novo_guardados.append(guardados[i])
        i = i + 1
    
    novo_guardados.append(rolados[indice])
    del(rolados[indice])
    lista_final = [rolados,novo_guardados]
    return lista_final

#retorna: uma lista com dois valores, o primeiro elemento da lista representando a lista de dados rolados e o segundo elemento representando a lista de dados armazenados no estoque

def remover_dado(rolados,guardados,indice2):
    lista_final2 = []
    
    rolados.append(guardados[indice2])
    del(guardados[indice2])
    lista_final2 = [rolados,guardados]
    return lista_final2

#recebe: uma lista de números inteiros representando as faces dos dados rolados
#retorna: dicionário com o cálculo dos pontos de acordo com o que foi descrito acima

def calcula_pontos_regra_simples(faces):
    indice1 = 0
    indice2= 0
    indice3 = 0
    indice4 = 0
    indice5 = 0
    indice6 = 0
    for i in faces:
        if i == 1:
            indice1 += 1
        if i == 2:
            indice2 += 2
        if i == 3:
            indice3 += 3
        if i == 4:
            indice4 += 4
        if i == 5:
            indice5 += 5
        if i == 6:
            indice6 += 6

    dicionario = {}
    dicionario[1] = indice1
    dicionario[2] = indice2
    dicionario[3] = indice3
    dicionario[4] = indice4
    dicionario[5] = indice5
    dicionario[6] = indice6

    return dicionario

def calcula_pontos_soma(faces):
    soma = 0
    for i in faces:
        soma = soma + i
    return soma


def calcula_pontos_sequencia_baixa(faces):
    if len(faces) < 4:
        return 0
    else: 
        faces_nova = []
        for i in faces:
            if i not in faces_nova:
                faces_nova.append(i)
        contagem = 1
        faces_nova.sort()
        for j in range(len(faces_nova) - 1):
            if faces_nova[j] + 1 == faces_nova[j + 1]:
                    contagem = contagem + 1
            else:
                if contagem < 4:
                    contagem = 0
        if contagem >= 4:
                return 15
        else:
                return 0
               
    
        



