import unittest

L = list()

# setupUpClass ---> np connection


class TestList(unittest.TestCase):

    def setUp(self):
        print("setUp x")
        L.clear()

    def tearDown(self):
        print("tearDown x")

    def test_listisempty(self):
        assert not L

    def test_append(self):
        L.append(1)
        assert L
