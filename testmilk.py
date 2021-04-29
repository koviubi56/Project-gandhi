import unittest
import dc


class TestDc(unittest.TestCase):

    def test_cmd(self):
        self.assertTrue(dc.cmd({"content":"56!testCommand"}, "56!", "testCommand"))

if __name__ == '__main__':
    unittest.main()
