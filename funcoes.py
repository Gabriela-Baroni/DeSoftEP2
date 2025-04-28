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
    novo_guardados = [guardados]
    novo_rolados = [rolados]
    novo_guardados.append(rolados[indice])
    novo_rolados.remove(rolados[indice])
    lista_final = [novo_rolados,novo_guardados]
    return lista_final