import unittest

import json
import os
import random

class TestJsonData(unittest.TestCase):
    def testHighscore(self):
        try:
            os.remove("data.json")
        except FileNotFoundError:
            print("data.json file not found")
        for i in range(1000):
            # random number as time taken
            time_taken = random.randint(0, 100)
            # try to open highscore.json file. If it doesn't exist, make it
            try:
                with open("data.json", 'r') as highscore_file:
                    data = json.load(highscore_file)
            except FileNotFoundError:
                with open("data.json", 'w') as highscore_file:
                    data = {
                        "highscore" : time_taken+1
                    }
                    json.dump(data, highscore_file)
            
            # time and highscore logic below:
            
            highscore = data["highscore"]
            if time_taken < data["highscore"]:
                # if time taken is less than highscore, set new highscore and print highscore message
                data["highscore"] = time_taken
                with open("data.json", 'w') as highscore_file:
                    json.dump(data, highscore_file)
                highscore = data["highscore"]
                print(f"\nHIGHSCORE! You took {time_taken} seconds to complete the test.")
            else:
                # else, print normal message that is not highscore
                # also print your previous highscore
                print(f"\nYou took {time_taken} seconds to complete the test. Good job!")
                highscore = data["highscore"]
                print(f"Previous highscore: {highscore}")
                
            # TEST
            with open("data.json", 'r') as highscore_file:
                data = json.load(highscore_file)
                self.assertEqual(data["highscore"], highscore)

        
if __name__ == "__main__":
    unittest.main()