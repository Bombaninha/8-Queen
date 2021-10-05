import unittest
import eight_queens
#import timer

class TestEightQueens(unittest.TestCase):
    # Conflict
    def test_conflict(self):
        board = [2, 2, 4, 8, 1, 6, 3, 4]

        self.assertEqual(10, eight_queens.conflict(board))

    def test_conflict2(self):
        board = [7, 2, 4, 8, 1, 6, 3, 4]

        self.assertEqual(8, eight_queens.conflict(board))

    def test_conflict3(self):
        board = [7, 2, 4, 8, 1, 8, 3, 4]

        self.assertEqual(6, eight_queens.conflict(board))

    def test_conflict_without_conflicts(self):
        board = [3, 5, 2, 8, 1, 7, 4, 6]
        
        self.assertEqual(0, eight_queens.conflict(board))

    # Evaluate
    def test_evaluate(self):
        board = [2, 2, 4, 8, 1, 6, 3, 4]

        self.assertEqual(10, eight_queens.evaluate(board))

    def test_evaluate2(self):
        board = [7, 2, 4, 8, 1, 6, 3, 4]

        self.assertEqual(8, eight_queens.evaluate(board))

    def test_evaluate3(self):
        board = [7, 2, 4, 8, 1, 8, 3, 4]

        self.assertEqual(6, eight_queens.evaluate(board))

    def test_evaluate_without_conflicts(self):
        board = [3, 5, 2, 8, 1, 7, 4, 6]

        self.assertEqual(0, eight_queens.evaluate(board))

    # Order Participants By Conflict 
    def test_order_participants_by_conflict(self):

        participants = [
            [2, 2, 4, 8, 1, 6, 3, 4],  # 10 conflitos
            [2, 7, 4, 8, 1, 6, 3, 4],  # 8 conflitos
        ]  

        result = [
           [2, 7, 4, 8, 1, 6, 3, 4], 
           [2, 2, 4, 8, 1, 6, 3, 4],
        ]

        self.assertEqual(result, eight_queens.order_participants_by_conflict(participants))   

    def test_order_participants_by_conflict2(self):

        participants = [
            [2, 2, 4, 8, 1, 6, 3, 4],  # 10 conflitos
            [7, 2, 4, 8, 1, 6, 3, 4],  # 8 conflitos
            [7, 2, 4, 8, 1, 8, 3, 4],  # 6 conflitos
            [3, 5, 2, 8, 1, 7, 4, 6],  # 0 conflitos
        ]  

        result = [
           [3, 5, 2, 8, 1, 7, 4, 6], 
           [7, 2, 4, 8, 1, 8, 3, 4],
           [7, 2, 4, 8, 1, 6, 3, 4],
           [2, 2, 4, 8, 1, 6, 3, 4],
        ]

        self.assertEqual(result, eight_queens.order_participants_by_conflict(participants))

    # Tournament
    def test_tournament(self):
        participants = [
            [2, 2, 4, 8, 1, 6, 3, 4],  # 10 conflitos
            [2, 7, 4, 8, 1, 6, 3, 4],  # 8 conflitos
        ]

        self.assertEqual([2, 7, 4, 8, 1, 6, 3, 4], eight_queens.tournament(participants))

    def test_tournament2(self):

        participants = [
            [2, 2, 4, 8, 1, 6, 3, 4],  # 10 conflitos
            [7, 2, 4, 8, 1, 6, 3, 4],  # 8 conflitos
            [7, 2, 4, 8, 1, 8, 3, 4],  # 6 conflitos
            [3, 5, 2, 8, 1, 7, 4, 6],   # 0 conflitos
        ]

        self.assertEqual([3, 5, 2, 8, 1, 7, 4, 6], eight_queens.tournament(participants))

    def test_tournament3(self):

        participants = [
            [7, 2, 4, 8, 1, 6, 3, 4],  # 8 conflitos
            [7, 2, 4, 8, 1, 8, 3, 4],  # 6 conflitos
        ]

        self.assertEqual([7, 2, 4, 8, 1, 8, 3, 4], eight_queens.tournament(participants))
   
    # Crossover
    def test_crossover(self):
        parent1 = [2, 4, 7, 4, 8, 5, 5, 2]
        parent2 = [3, 2, 7, 5, 2, 4, 1, 1]

        offspring1, offspring2 = eight_queens.crossover(parent1, parent2, 3)

        children = [offspring1, offspring2]

        self.assertIn([2, 4, 7, 5, 2, 4, 1, 1], children)
        self.assertIn([3, 2, 7, 4, 8, 5, 5, 2], children)

    def test_crossover2(self):
        parent1 = [2, 4, 7, 4, 8, 5, 5, 2]
        parent2 = [3, 2, 7, 5, 2, 4, 1, 1]

        offspring1, offspring2 = eight_queens.crossover(parent1, parent2, 2)

        children = [offspring1, offspring2]

        self.assertIn([3, 2, 7, 4, 8, 5, 5, 2], children)
        self.assertIn([2, 4, 7, 5, 2, 4, 1, 1], children)

    def test_crossover_zero_genes(self):
        parent1 = [7, 2, 4, 8, 1, 8, 3, 4]
        parent2 = [3, 5, 2, 8, 1, 7, 4, 6]

        offspring1, offspring2 = eight_queens.crossover(parent1, parent2, 0)

        children = [offspring1, offspring2]

        self.assertIn([7, 2, 4, 8, 1, 8, 3, 4], children)
        self.assertIn([3, 5, 2, 8, 1, 7, 4, 6], children)

    def test_crossover_all_genes(self):
        parent1 = [2, 4, 7, 4, 8, 5, 5, 2]
        parent2 = [3, 2, 7, 5, 2, 4, 1, 1]

        offspring1, offspring2 = eight_queens.crossover(parent1, parent2, 8)

        children = [offspring1, offspring2]

        self.assertIn([2, 4, 7, 4, 8, 5, 5, 2], children)
        self.assertIn([3, 2, 7, 5, 2, 4, 1, 1], children)

    # Mutate
    def test_mutate_prob_zero(self):
        """
        Teste simples: mutacao com prob = 0 deve retornar o individuo intacto
        :return:
        """
        original = [2, 4, 7, 4, 8, 5, 5, 2]
        mutated = eight_queens.mutate(original[:], 0)  # sends a copy of 'original'
        self.assertEqual(original, mutated)

    def test_mutate_prob_one(self):
        """
        Teste simples: mutacao com prob = 1 deve retornar um individuo diferente.
        Porem, pode haver o 'azar' da mutacao sortear o mesmo numero que ja estava.
        Assim, se esse teste falhar, rode-o novamente para verificar se a falha foi
        devido ao azar ou se o codigo esta mesmo com problema.
        :return:
        """
        original = [2, 4, 7, 4, 8, 5, 5, 2]
        mutated = eight_queens.mutate(original[:], 1)  # sends a copy of 'original'
        self.assertNotEqual(original, mutated)

    # Aleatorios
    def test_aleatorios(self):
        participantes_aleatorios = eight_queens.aleatorios(5)
        self.assertEqual(5, len(participantes_aleatorios))

    def test_aleatorios2(self):
        participantes_aleatorios = eight_queens.aleatorios(30)
        self.assertEqual(30, len(participantes_aleatorios))

    def test_aleatorios_without_participants(self):
        participantes_aleatorios = eight_queens.aleatorios(0)
        self.assertEqual(0, len(participantes_aleatorios))

    # Unif Aleat
    def test_unif_aleat(self):
        participants = [
            [2, 2, 4, 8, 1, 6, 3, 4], 
            [7, 2, 4, 8, 1, 6, 3, 4], 
            [7, 2, 4, 8, 1, 8, 3, 4],  
            [3, 5, 2, 8, 1, 7, 4, 6],  
        ]

        k = 3

        self.assertEqual(3, len(eight_queens.unif_aleat(participants, k)))

    def test_unif_aleat2(self):
        participants = [
            [2, 2, 4, 8, 1, 6, 3, 4], 
            [7, 2, 4, 8, 1, 6, 3, 4], 
            [7, 2, 4, 8, 1, 8, 3, 4],  
            [3, 5, 2, 8, 1, 7, 4, 6],  
        ]

        k = 4
        
        self.assertEqual(4, len(eight_queens.unif_aleat(participants, k)))

    def test_unif_aleat_zero(self):
        participants = [
            [2, 2, 4, 8, 1, 6, 3, 4], 
            [7, 2, 4, 8, 1, 6, 3, 4], 
            [7, 2, 4, 8, 1, 8, 3, 4],  
            [3, 5, 2, 8, 1, 7, 4, 6],  
        ]

        k = 0
        
        self.assertEqual(0, len(eight_queens.unif_aleat(participants, k)))

    # Top
    def test_top(self):
        participants = [
            [2, 2, 4, 8, 1, 6, 3, 4],  # 10 conflitos
            [7, 2, 4, 8, 1, 6, 3, 4],  # 8 conflitos
            [7, 2, 4, 8, 1, 8, 3, 4],  # 6 conflitos
            [3, 5, 2, 8, 1, 7, 4, 6],  # 0 conflitos
        ]  

        result = [
           [3, 5, 2, 8, 1, 7, 4, 6], 
           [7, 2, 4, 8, 1, 8, 3, 4],
           [7, 2, 4, 8, 1, 6, 3, 4],
        ]

        self.assertEqual(result, eight_queens.top(3, participants))   

    def test_top_0(self):
        participants = [
            [2, 2, 4, 8, 1, 6, 3, 4],  # 10 conflitos
            [7, 2, 4, 8, 1, 6, 3, 4],  # 8 conflitos
            [7, 2, 4, 8, 1, 8, 3, 4],  # 6 conflitos
            [3, 5, 2, 8, 1, 7, 4, 6],  # 0 conflitos
        ]  

        result = []

        self.assertEqual(result, eight_queens.top(0, participants)) 

    def test_top_1(self):
        participants = [
            [2, 2, 4, 8, 1, 6, 3, 4],  # 10 conflitos
            [7, 2, 4, 8, 1, 6, 3, 4],  # 8 conflitos
            [7, 2, 4, 8, 1, 8, 3, 4],  # 6 conflitos
            [3, 5, 2, 8, 1, 7, 4, 6],  # 0 conflitos
        ]  

        result = [
            [3, 5, 2, 8, 1, 7, 4, 6], 
        ]

        self.assertEqual(result, eight_queens.top(1, participants))   
'''
    def test_run_ga(self):
        """
        Testa APENAS se o algoritmo executa no tempo especificado.
        Nao avalia a qualidade da solucao encontrada nem a corretude da implementacao
        :return:
        """
        response = timer.timeout(
            eight_queens.run_ga,
            args=(100, 40, 2, 0.3, True),
            time_limit=60, default='timeout'
        )
        if response == 'timeout':
            self.fail("run_ga ran out of time")
'''

if __name__ == '__main__':
    unittest.main()
