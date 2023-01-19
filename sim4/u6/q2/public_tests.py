import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global oculta_letras
        undertest = __import__(module)
        oculta_letras = getattr(undertest, 'oculta_letras', None)

    def test_tipo_exemplo(self):
        assert oculta_letras("Casa", "a") == "_a_a"
        assert oculta_letras("Casa", "c") == "C___"
        assert oculta_letras("Casa", "aS") == "_asa"

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
