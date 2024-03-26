import json
import os

from config import *

def save_state(progress, fz, v):
        #save game
        with open(os.path.join(WORKING_DIR, "JSONs", "GameState.json"), "r") as f:
            data = json.load(f)
            memory_turns = data.get("memory_turns", 0)
            f.close()

        with open(os.path.join(WORKING_DIR, "JSONs", "GameState.json"), "w") as f:
            data = {
                "progress": progress,
                "memory_turns": memory_turns or 0
            }
            json.dump(data, f, indent=4)
        with open(os.path.join(WORKING_DIR, "JSONs", "settings.json"), "w") as f:
            data = {
                "volume": v,
                "font_size": fz,
            }
            json.dump(data, f, indent=4)