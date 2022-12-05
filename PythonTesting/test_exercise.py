import unittest

def str_to_bool(value):
    #true_values = ['y','yes']
    # false_values = ['no', 'n']
    # if value in true_values:
    # return True
    # if value in false_values:
    # #return False
    try:     # raises an AttributeError if a non-string value is used
        value = value.lower()
    except AttributeError:
        raise AttributeError(f"{value} must be of type string")
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False

class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('yes') #FAILURE TEST : When Yes is captilaized: File "test_exercise.py", line 20, in test_yes_is_true self.assertTrue(result) AssertionError: None is not true
        self.assertTrue(result)
    
    def test_invalid_input(self): #should verify that the AttributeError raises on non-string input
        with self.assertRaises(AttributeError):
            str_to_bool(1)

if __name__ == '__main__':
    unittest.main()
    
