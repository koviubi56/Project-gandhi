import unittest
import dc
import main


class TestDc(unittest.TestCase):

    def test_cmd(self):
        self.assertTrue(dc.cmd({"content":"56!testCommand"}, "56!", "testCommand"))

class TestMain(unittest.TestCase):

    def test_backup_realInfo(self):
        bu = main.backup("AUTO", True)
        self.assertEqual(bu["AUTObackup"]["szerdak"], db["szerdak"])

"""
    def test_backup_equal(self):
        old = db["backup"]
        new = main.backup("AUTO", True)
        self.assertNotEqual(old, new)
"""

if __name__ == '__main__':
    unittest.main()
