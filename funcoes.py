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
    novo_rolados = []
    
    novo_rolados.append(rolados[indice2])
    del(guardados[indice2])
    lista_final2 = [novo_rolados,guardados]
    return lista_final2