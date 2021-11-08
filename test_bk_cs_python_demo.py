import unittest
from bk_cs_python_demo.bk_cs_python_demo import name_here

class Test(unittest.TestCase):
    def test_name_here(self):
        output = name_here('ciara')
        print("output of name_ere: {}".format(output))
        self.assertEquals('ciara was ere', output)
