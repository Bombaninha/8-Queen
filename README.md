# Trabalho 3

## Integrantes

| Turma |             Nome            |  Cartão  |
|:-----:|:---------------------------:|:--------:|
|   B   |   Henrique Zanotto Vazatta  | 00303532 |
|   A   |    Lucas Spagnolo Bombana   | 00314879 |
|   B   | Pablo Yuri Scherer de Souza | 00291589 |

### Eight Queens

#### Informações percebidas

Algumas coisas que percebemos:

* Um número muito grande de gerações acabava estreitando os dados.
* Em algum momento a média, o maior valor e o menor valor acabavam ficando aproximados.
* Um número muito alto na probabilidade de mutação poderia estragar o melhor resultado obtido.
* Um número muito baixo na probabilidade de mutação poderia deixar o conjunto meio "parado".

#### Resultado

![Resultados](https://user-images.githubusercontent.com/40179398/136102991-3072d5b5-c03f-47f9-9a3a-eae233026677.png)

* Número de conflitos do melhor indivíduo retornado pela função: 8
* Geração com maior número de conflitos: Geração 61 com 14 conflitos.
* Geração com menor número de conflitos: Geração 88 com 3 conflitos.
* Geração com maior média de conflitos: Geração 61 com média de 14 conflitos.
* Geração com menor média de conflitos: Geração 88 com média de 3 conflitos.

#### Parâmetros

Para os resultados obtidos, utilizamos a seguinte chamada:

* Número de gerações (_g_): 100
* Número de indivíduos (_n_): 15
* Número de participantes do torneio (_k_): 2
* Probabilidade de mutação (_m_): 0.15
* Vai haver elitismo (_e_): True

#### Dificuldades

Estranhamos que, apesar de seguir o algoritmo dado em aula e utilizarmos parâmetros semelhantes, o gráfico acabou ficando bem diferente do fornecido no enunciado do trabalho. Parece que os dados, em algum momento, passaram a ser comprimidos resultando nos mesmos valores.

### Alegrete

#### Parâmetros

* theta_0: -3.1
* theta_1: -1.11
* alpha: 0.01
* num_iterations: 500

#### Resultado

Com esses valores chegamos a um erro quadrático final de: 8.959027357713508


