import unittest     # Import the Python unit testing framework
from logger import Logger       # Our code to test
from Target import Target

class LoggerTest(unittest.TestCase):
    ''' Unit tests for our logger functions. '''
   
    def test_info(self):
        t = Target() #create a target stub
        log = Logger(target=t.set_text)#passing a function as a parameter because functions are objects in Python
        log.info('hello')#set text
        actual = t.get_text()
        self.assertEqual(actual, '[INFO] hello')
        
    def test_error(self):
        t = Target()
        log = Logger(target=t.set_text)
        log.error('error')
        actual = t.get_text()
        self.assertEqual(actual, '[WARNING] error')
        
        
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()  
