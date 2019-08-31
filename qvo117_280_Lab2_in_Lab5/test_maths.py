import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add_with_new_parameter(self):
        actual = maths.add(5, 5, 2)
        self.assertEqual(actual, '1010')
    
    
    
    def test_add(self):
        ''' Tests the add function. '''
        #Arrange and Act
        actual = maths.add(0, 1)
        #Assert
        self.assertEqual(actual, 1)
       

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        actual = maths.fibonacci(5)
        self.assertEqual(actual, 5)
        
     
    
    def test_convert_base_under_10(self):
        actual = maths.convert_base(10, 2)
        self.assertEqual(actual, '1010')
        
    
    def test_convert_base_over_10(self):
        actual = maths.convert_base(10, 16)
        self.assertEqual(actual, 'A')
        
    def test_factorial(self):
        ''' Tests the factorial function. '''
        actual = maths.factorial(3)
        self.assertEqual(actual, 6)


# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
