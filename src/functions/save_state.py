import json
import os

from config import *

def save_state(progress, sp, fz, v):
        #save game
        with open(os.path.join(WORKING_DIR, "JSONs", "GameState.json"), "r") as f:
            data = json.load(f)
            memory_turns = data.get("memory_turns", 0)
            space_bags_cleared = data.get("space_bags_cleared", 0)
            f.close()

        with open(os.path.join(WORKING_DIR, "JSONs", "GameState.json"), "w") as f:
            data = {
                "progress": progress,
                "secret_progress": sp,
                "memory_turns": memory_turns or 0,
                "space_bags_cleared": space_bags_cleared or 0
            }
            json.dump(data, f, indent=4)

        with open(os.path.join(WORKING_DIR, "JSONs", "settings.json"), "w") as f:
            data = {
                "volume": v,
                "font_size": fz,
            }
            json.dump(data, f, indent=4)