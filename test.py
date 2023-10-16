from unittest import TestCase

from equations import discriminant, solution
from vote import vote
from secretary import get_name, get_directory


class TestEquations(TestCase):
    def setUp(self):
        self.datas = ((1, 8, 15), (1, -13, 12), (-4, 28, -49), (1, 1, 1))
        self.result = ((-3.0, -5.0), (12.0, 1.0), 3.5, 'корней нет')
    
    def test_equations(self):
        for index,  data in enumerate(self.datas):
            a, b, c = data
            result = solution(a, b, c)
            if isinstance(result, tuple):
                self.assertTupleEqual(result, self.result[index])
            else:
                self.assertEqual(result, self.result[index])


class TestVote(TestCase):
    def setUp(self):
        self.datas = ([1,1,1,2,3], [1,2,3,2,2])
        self.result = (1, 2)
    
    def test_vote(self):
        for index,  data in enumerate(self.datas):
            self.assertEqual(vote(data), self.result[index])


class TestSecretary(TestCase):
    def setUp(self):
        self.datas_name = ('10006', '101', '311 020203')
        self.result_name = ('Аристарх Павлов', 'Документ не найден', 'Документ не найден')

        self.datas_directory = ('11-2', '311 020203', '10006')
        self.result_directory = ('1', 'Полки с таким документом не найдено', '2')
    
    def test_get_name(self):
        for index,  data in enumerate(self.datas_name):
            self.assertEqual(get_name(data), self.result_name[index])
    
    def test_get_directory(self):
        for index,  data in enumerate(self.datas_directory):
            self.assertEqual(get_directory(data), self.result_directory[index])
            