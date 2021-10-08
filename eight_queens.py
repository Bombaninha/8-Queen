import random
#import matplotlib.pyplot as plt

def conflict(board):
    n = len(board)
    
    row_frequency = [0] * n
    main_diag_frequency = [0] * (2 * n)
    secondary_diag_frequency = [0] * (2 * n)

    for i in range(n):
        row_frequency[board[i] - 1] += 1
        main_diag_frequency[board[i] - 1 + i] += 1
        secondary_diag_frequency[n - board[i] - 1 + i] += 1

    conflicts = 0

    for i in range(2 * n):
        if i < n:
            conflicts += (row_frequency[i] * (row_frequency[i] - 1)) / 2
        conflicts += (main_diag_frequency[i] * (main_diag_frequency[i] - 1)) / 2
        conflicts += (secondary_diag_frequency[i] * (secondary_diag_frequency[i] - 1)) / 2
    return int(conflicts)

def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 9.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    return conflict(individual)

def order_participants_by_conflict(participants):
    return sorted(participants, key=lambda individuo: conflict(individuo))

def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    best = order_participants_by_conflict(participants)
    return best.pop(0)

def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    parent1[:index], parent2[:index] = parent2[:index], parent1[:index] 
    return parent1, parent2

def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    if(random.random() < m):
        pos = random.choice([0, 1, 2, 3, 4, 5, 6, 7])
        value = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
        individual[pos] = value
    
    return individual

def aleatorios(n):
    individuos = []
    for i in range(n):
        individuo = [0] * 8
        for j in range(8):
            individuo[j] = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
        individuos.append(individuo)
    return individuos

def unif_aleat(populacao, k):
    individuos = []
    for i in range(k):
        pos = random.randrange(0, len(populacao), 1)
        individuos.append(populacao[pos])
    return individuos

def top(qtde, populacao):
    populacao_ordenada = order_participants_by_conflict(populacao)
    return populacao_ordenada[0:qtde]

def selecao(populacao, k):
    participantes_round1 = unif_aleat(populacao, k)    
    p1 = top(1, participantes_round1)[0]

    participantes_round2 = unif_aleat(populacao, k)
    p2 = top(1, participantes_round2)[0]
    return p1, p2

def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :return:list - melhor individuo encontrado
    """
    
    # Variaveis para gerar o grafico
    #generations_max = []
    #generations_min = []
    #generations_mean = []
    #x = range(g)

    p = aleatorios(n)
    #print("Populacao gerada aleatoriamente com tamanho " + str(n) + ": " + str(p))

    while(g > 0):
        pl = top(1, p) if e else []
        while(len(pl) < n):
            p1, p2 = selecao(p, k)

            #print("Selecao: ") 
            #print(p1, p2)
            o1, o2 = crossover(p1, p2, random.choice([0, 1, 2, 3, 4, 5, 6, 7]))

            #print("Crossover: ")
            #print(o1, o2)

            o1 = mutate(o1, m)
            o2 = mutate(o2, m)

            #print("Mutate: ")
            #print(o1, o2)

            pl.append(o1)
            pl.append(o2)
            #print("P': ")
            #print(pl)
            #print("-"*20)
        p = pl
        #print("Geracao: " + str(g))
        #print("Populacao: ")
        #print(p)
        sorted_population = order_participants_by_conflict(p)
        #list = []
        #print(sorted_population)
        #for i in sorted_population:
        #    list.append(conflict(i))
        #print(list)
        #print("Populacao Ordenada: ")
        #print(sorted_population)
        #print("Top 1: ")
        #print(top(1, p)[0])
        #print("Valor do top 1: ")
        #print(evaluate(top(1, p)[0]))
        #print("-" * 20)
        
        #generations_max.append(conflict(sorted_population[len(sorted_population) - 1]))
        #generations_min.append(conflict(sorted_population[0]))
        #soma = 0
        #for i in sorted_population:
        #    soma += conflict(i)
        #mean = soma / len(sorted_population)
        #generations_mean.append(mean)

        #print("maior")
        #print(generations_max)
        #print("menor")
        #print(generations_min)
        #print("media")
        #print(generations_mean)
        #print("-" * 20)
        g = g - 1

    #print(len(x),len(generations_max),len(generations_min),len(generations_mean))
    #print(evaluate(top(1, p)[0]))
    #plt.plot(x, generations_max, c='green', label = 'Maior número de conflitos')
    #plt.plot(x, generations_min, c='blue', label = 'Menor número de conflitos')
    #plt.plot(x, generations_mean, c='red', label = 'Média do número de conflitos')
    #plt.ylabel('Número de Conflitos')
    #plt.xlabel('Gerações')
    #plt.title("Relação Geração X Conflitos")
    #plt.legend()
    #plt.show()
    return top(1, p)[0]
    #return top(1, p)[0], generations_max, generations_min, generations_mean

#teste = run_ga(15, 5, 2, 0.2, True)