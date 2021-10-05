import numpy as np


def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    sum = 0
    cont = 0
    for row in data:
        sum += pow((theta_0 + (row[0] * theta_1) - row[1]), 2)
        cont += 1
    mse = sum / cont
    return mse


def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    sum0 = 0
    sum1 = 0
    cont = 0
    for row in data:
        sum0 += (theta_0 + (row[0] * theta_1) - row[1]) * 2
        sum1 += (theta_0 + (row[0] * theta_1) - row[1]) * row[0] * 2
        cont += 1
    dmse0 = sum0 / cont
    dmse1 = sum1 / cont

    theta_0 = theta_0 - alpha * dmse0
    theta_1 = theta_1 - alpha * dmse1
    return theta_0, theta_1



def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """

    theta_0_list = []
    theta_1_list = []
    current_iterations = 0
    currentTheta_1 = theta_1
    currentTheta_0 = theta_0
    while num_iterations > current_iterations:

        iteration = step_gradient(currentTheta_0, currentTheta_1 , data, alpha)

        currentTheta_0 = iteration[0]
        currentTheta_1 = iteration[1]

        theta_0_list.append(currentTheta_0)
        theta_1_list.append(currentTheta_1)

        current_iterations += 1
    
    return theta_0_list, theta_1_list
