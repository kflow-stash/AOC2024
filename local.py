import json
import pandas  as pd

input_ = json.loads(open("data/local_json.txt","r").read())

rows = []
for member in input_["members"].values():
    name_ = member["name"]
    completions_ = member["completion_day_level"]
    for day_id, parts in completions_.items():
        for part_id, stats in parts.items():
            rows.append({"name":name_, "day": int(day_id), "part": int(part_id), "timestamp": int(stats["get_star_ts"])})
            
df = pd.DataFrame(rows)

df["datetime"] = pd.to_datetime(pd.Timestamp(df["timestamp"]))

df = df.sort_values("datetime").reset_index(drop=True)


stop_here = 1