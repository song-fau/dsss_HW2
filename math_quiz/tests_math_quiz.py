import unittest
from math_quiz import get_randomnumber, get_operator, get_problemandanswer


class TestMathGame(unittest.TestCase):

    def test_get_randomnumber(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_randomnumber(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_operator(self):
        #test if operators are choiced in the list
        #TODO
        operators = ['+','-','*']
        for _ in range(1000):# test a large number of operators
            rand_operator = get_operator()
            self.assertIn(rand_operator,operators)

    def test_get_problemandanswer(self):
        #test if the problems and answers are equal to the expected problems and answers
            test_cases = [
                (5,2,'+','5 + 2',7),
                (6,2,'-','6 - 2',4),
                (7,3,'*','7 * 3',21),
                (7,3,'-','7 - 3',4),
                (6,5,'*','6 * 5',30),
                (10,3,'+','10 + 3',13),
                (5,3,'+','5 + 3',8),
                (9,6,'*','9 * 6',54)
                ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                problem, answer = get_problemandanswer(num1,num2,operator)
                self.assertEqual(problem,expected_problem)
                self.assertEqual(answer,expected_answer)
                
                
                

if __name__ == "__main__":
    unittest.main()
