import os
import unittest
from unittest import mock
import unit_test_examples.tools.json_reader as jr

# set working dir to the location of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class TestJsonReader(unittest.TestCase):
    """Tests various functions in the json_reader module.
    """

    def setUp(self):
        self.LARGE_JSON_CONTENTS = {
            "quiz": {
                "sport": {
                    "q1": {
                        "question": "Which one is correct team name in NBA?",
                        "options": [
                            "New York Bulls",
                            "Los Angeles Kings",
                            "Golden State Warriros",
                            "Huston Rocket"
                        ],
                        "answer": "Huston Rocket"
                    }
                }
            }
        }

    def tearDown(self):
        pass


    @mock.patch('json.load', return_value={
        "fruit": "Orange",
        "size": "Medium",
        "color": "Orange"
    })
    def test_reading_simple_json_file(self, mock_json):
        json_data = jr.read_json('../data/data1.json')
        self.assertEqual(json_data['fruit'], 'Orange')
        self.assertEqual(json_data['size'], 'Medium')

    def test_reading_larger_json_file(self):
        with mock.patch('json.load', return_value=self.LARGE_JSON_CONTENTS):
            json_data = jr.read_json('../data/data2.json')
            self.assertEqual(json_data['quiz']['sport']['q1']['answer'], 'Huston Rocket')


if __name__ == '__main__':
    unittest.main()