import unittest

class TestAssertions(unittest.TestCase):

    def test_equals(self):
        self.assertEqual("one string", "one string")
        #self.assertEqual("one string", "other string")
        #This will result in an assertion failure because the strings are different. 

     
if __name__ == '__main__':
    unittest.main()

#RUNNING TEST 
#METHOD 1 - python FILENAME.py
#METHOD 2 - python -m unittest (tests can be discovered automatically)

# a test for customer accounts that verify creation and deletion
class TestAccounts(unittest.TestCase):

    def test_creation(self):
        self.assertTrue(account.create())

    def test_deletion(self):
        self.assertTrue(account.delete())