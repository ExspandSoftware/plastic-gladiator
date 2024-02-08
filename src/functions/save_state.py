import json
import os

from config import *

def save_state(self):
        #save game
        with open(os.path.join(WORKING_DIR, "JSONs", "GameState.json"), "w") as f:
            data = {
                "progress": self.progress,
            }
            json.dump(data, f, indent=4)