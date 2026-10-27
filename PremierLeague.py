import soccerdata as sd
import pandas as pd
import time

all_shots = []

# Collect data from 2016-17 season to 2025-26 season
for season_year in range(16, 26):
    season = f"{str(season_year)}-{str(season_year + 1)}"

    print(f"Downloading {season}...", flush=True)

    understat = sd.Understat("ENG-Premier League", season)
    print("Starting request", flush=True)
    shots = understat.read_shot_events()
    print("Request finished", flush=True)

    print(f"Collected {len(shots)} shots")
    all_shots.append(shots)

    time.sleep(1)

print("Finished downloading all seasons")

epl_shots = pd.concat(all_shots, ignore_index=True)

epl_shots.to_csv("epl_shots_2016_2025.csv", index=False)
