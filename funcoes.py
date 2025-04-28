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
    dicionario = {}
    dicionario [1] = 0
    dicionario [2] = 0
    dicionario [3] = 0
    dicionario [4] = 0
    dicionario [5] = 0
    dicionario [6] = 0
    for i in faces:
        if i == 1:
            dicionario[1] += 1
        if i == 2:
            dicionario[2] += 2
        if i == 3:
            dicionario[3] += 3
        if i == 4:
            dicionario[4] += 4
        if i == 5:
            dicionario[5] += 5
        if i == 6:
            dicionario[6] += 6

        return dicionario

