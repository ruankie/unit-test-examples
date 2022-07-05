import os
import unittest
import unit_test_examples.tools.json_reader as jr

# set working dir to the location of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class TestJsonReader(unittest.TestCase):
    """Tests various functions in the json_reader module.
    """

    def test_reading_json_file(self):
        json_data = jr.read_json('../data/data1.json')
        self.assertEqual(json_data['fruit'], 'Apple')

        json_data = jr.read_json('../data/data2.json')
        self.assertEqual(json_data['quiz']['maths']['q2']['answer'], '4')
        


if __name__ == '__main__':
    unittest.main()