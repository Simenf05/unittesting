import unittest
import methods as ss


def adder_function(term1, term2):
    return term1 + term2



class Test_adder_function(unittest.TestCase):
    
    
    def test_fizzbuzz_none(self):
        expected = None
        actual = ss.fizzbuzz(2)
        self.assertEqual(actual, expected)
    
    
    def test_fizzbuzz_buzz(self):
        expected = "buzz"
        actual = ss.fizzbuzz(3)
        self.assertEqual(actual, expected)
    
    
    def test_fizzbuzz_fizz(self):
        expected = "fizz"
        actual = ss.fizzbuzz(5)
        self.assertEqual(actual, expected)
    
    
    def test_fizzbuzz_fizzbuzz(self):
        expected = "fizzbuzz"
        actual = ss.fizzbuzz(15)
        self.assertEqual(actual, expected)
    
    
    def test_selection_sort_correct_order(self):
        expected = [1, 2, 3]
        actual = ss.selection_sort([3, 2, 1])
        self.assertEqual(actual, expected)
        
        
    def test_selection_sort_type_of_input_value(self):
        with self.assertRaises(TypeError):
            ss.selection_sort(tuple([1, 2, 3]))
        
    
    def test_selection_sort_mutability_of_input_value(self):
        with self.assertRaises(TypeError):
            ss.selection_sort(tuple([1, 2, 3]))
            
            
    def test_selection_sort_string_list(self):
        expected = ["a", "b", "c"]
        actual = ss.selection_sort(["c", "a", "b"])
        self.assertEqual(actual, expected)

    
    def test_number_input(self):
        expected = 4
        actual = adder_function(2, 2)
        
        self.assertEqual(actual, expected)
        
        
    def test_number_input2(self):
        expected = 8
        actual = adder_function(5, 3)
        
        self.assertEqual(actual, expected)
    
    
    def test_string_input(self):
        expected = "hello world"
        actual = adder_function("hello ", "world")
        
        self.assertEqual(actual, expected)
        
        
    def test_different_type_input(self):
        with self.assertRaises(TypeError):
            adder_function("1", 1)
    