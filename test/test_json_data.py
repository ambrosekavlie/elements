import unittest

import sys
sys.path.append('src')

from elements import update_json_data

import json
import os
import random

class TestJsonData(unittest.TestCase):
    def testHighscore(self):
        try:
            os.remove("data.json")
        except FileNotFoundError:
            print("data.json file not found")
        
        highscore = 101
        for i in range(1000):
            # random number as time taken
            time_taken = random.randint(0, 100)
            if time_taken < highscore:
                highscore = time_taken
            
            update_json_data(time_taken)
                
            # TEST
            with open("data.json", 'r') as highscore_file:
                data = json.load(highscore_file)
                self.assertEqual(data["highscore"], highscore)
        
if __name__ == "__main__":
    unittest.main()
