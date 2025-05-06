import funcoes
from funcoes import *

cartela_de_pontos = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

rodada = 0
while rodada <= 12:
    rolados = rolar_dados(5)
    guardados = []
    opcao = int(input())
    rolagem = 0
    cada_rodada = True

    while cada_rodada == True:
        
        print("Dados rolados: {0}".format(rolados))
        print("Dados guardados: {0}".format(guardados))
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = int(input())
        

        #opção 1 (guardar um dado):
        if opcao == 1:
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            while indice < 0 or indice > len(rolados):
                print("Opção inválida. Tente novamente.")
                indice = int(input())
            if indice >= 0 and indice < len(rolados):
                guardar = guardar_dado(rolados,guardados,indice)

        #opção 2 (remover um dado):
        elif opcao == 2:
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice2 = int(input())
            while indice2 < 0 or indice2 > len(guardados):
                print("Opção inválida. Tente novamente.")
                indice2 = int(input())
            if indice2 >= 0 and indice2 < len(guardados):
                remover = remover_dado(rolados,guardados,indice2)

            
        #opção 3 (rolar novamente):
        elif opcao == 3:
            if rolagem < 2:
                tamanho = len(rolar)
                rolados = rolar_dados(tamanho)
                rolagem = rolagem + 1
            else:
                print("Você já usou todas as rerrolagens.")
        
        
        #opção 4 (verificar a cartela):
        elif opcao == 4:
            cartela = imprime_cartela(cartela)


        #opção 0 (fazer a jogada):
        elif opcao == 0:    
            dados = rolados + guardados
            print("Digite a combinação desejada:")
            string = str(input())
            
            if string in ["1","2","3","4","5","6"]:
                string_int = int(string)
                if string_int in cartela_de_pontos["regra_simples"]:
                    while cartela_de_pontos["regra_simples"][string_int] != -1:
                        print ("Essa combinação já foi utilizada.")
                    if cartela_de_pontos["regra_simples"][string_int] == -1:
                        jogada_simples = faz_jogada(dados, string_int, cartela_de_pontos)
                        cada_rodada = False
            
            elif string in cartela_de_pontos["regra_avancada"]:
                while cartela_de_pontos["regra_avancada"]["string"] == -1:
                    print("Essa combinação já foi utilizada.")
                if cartela_de_pontos["regra_avancada"]["string"] == -1:
                    jogada_avancada = faz_jogada(dados, string, cartela_de_pontos)
                    cada_rodada = False
            else:
                print("Combinação inválida, tente novamente.")
        else:
            print("Combinação inválida, tente novamente.")
        
    rodada = rodada + 1


cartela = imprime_cartela(cartela_de_pontos)


#total regra simples

total_s = 0
for ponto_s in cartela_de_pontos["regra_simples"].values():
    if ponto_s != 1:
        total_s = total_s + ponto_s

#total regra avançada

total_a = 0
for ponto_a in cartela_de_pontos["regra_avancada"].values():
    if ponto_a != 1:
        total_a = total_a + ponto_a

if total_s >= 63:
    extra = 35

else:
    extra = 0

total_f = total_s + total_a + extra


print (cartela) 
print("Pontuação total: {0}".format(total_f))