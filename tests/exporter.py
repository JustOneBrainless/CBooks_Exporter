import unittest

from src.exporter.exporter import Exporter


class TestExporter(unittest.TestCase):

    # Create an offer file

    def test_authenticate_wrong_datatype(self):
        e = Exporter()
        e.create_files()


if __name__ == '__main__':
    unittest.main()
