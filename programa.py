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

imprime_cartela(cartela_de_pontos)

rodada = 0
while rodada < 12:
    rolados = rolar_dados(5)
    guardados = []
    rolagem = 0
    cada_rodada = True

    while cada_rodada == True:
        
        print("Dados rolados: {0}".format(rolados))
        print("Dados guardados: {0}".format(guardados))
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        
        opcao_valida = False
        while not opcao_valida:
            opcao = input()

            if opcao.isdigit():
                opcao = int(opcao)
                if opcao >= 0 and opcao <= 4:
                    opcao_valida = True
                else:
                    print("Opção inválida. Tente novamente.")
            else:
                print("Opção inválida. Tente novamente.")
        
        #opção 1 (guardar um dado):
        if opcao == 1:
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = input()
            if indice.isdigit():
                indice_int = int(indice)
                if indice_int >= 0 and indice_int <= 4:
                    guardados.append(rolados.pop(indice_int))
                else:
                    print("Opção inválida. Tente novamente.")
            else:
                print("Opção inválida. Tente novamente.")

        #opção 2 (remover um dado):
        elif opcao == 2:
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice2 = input()
            if indice2.isdigit():
                indice2_int = int(indice2)
                if indice2_int >= 0 and indice2_int <= 4:
                    rolados.append(guardados.pop(indice2_int))
                else:
                        print("Opção inválida. Tente novamente.")
            else:
                print("Opção inválida. Tente novamente.")  
            

            
        #opção 3 (rolar novamente):
        elif opcao == 3:
            if rolagem < 2:
                rolagem = rolagem + 1
                tamanho = len(rolados)
                rolados = rolar_dados(tamanho)
            else:
                print("Você já usou todas as rerrolagens.")
        
        
        #opção 4 (verificar a cartela):
        elif opcao == 4:
            imprime_cartela(cartela_de_pontos)


        #opção 0 (fazer a jogada):
        elif opcao == 0:    
            dados = rolados + guardados
            jogada = False
            print("Digite a combinação desejada:")
            
            while jogada == False:
                string = input()

                if string == 'sem_combinacao' or string == 'quadra' or string == 'full_house' or string == 'sequencia_baixa' or string == 'sequencia_alta' or string == 'cinco_iguais':
                    if cartela_de_pontos['regra_avancada'][string] == -1:
                        faz_jogada(dados, string, cartela_de_pontos)
                        jogada = True
                        cada_rodada = False
                    else:
                        print("Essa combinação já foi utilizada.")
                
                elif string.isdigit():
                    string_int = int(string)
                    if string_int in cartela_de_pontos['regra_simples']:
                        if cartela_de_pontos['regra_simples'][string_int] == -1:
                            faz_jogada(dados, string, cartela_de_pontos)
                            jogada = True
                            cada_rodada = False
                        else:
                            print("Essa combinação já foi utilizada.")
                    else:
                        print("Combinação inválida. Tente novamente.")
                else:
                    print("Combinação inválida. Tente novamente.")

           
        
    rodada = rodada + 1


imprime_cartela(cartela_de_pontos)


#total regra simples

total_s = 0
for chave_s in cartela_de_pontos["regra_simples"]:
    ponto_s = cartela_de_pontos["regra_simples"][chave_s]
    if ponto_s != -1:
        total_s = total_s + ponto_s

#total regra avançada

total_a = 0
for chave_a in cartela_de_pontos["regra_avancada"]:
    ponto_a = cartela_de_pontos["regra_avancada"][chave_a]
    if ponto_a != -1:
        total_a = total_a + ponto_a

if total_s >= 63:
    extra = 35

else:
    extra = 0

total_f = total_s + total_a + extra

print("Pontuação total: {0}".format(total_f))