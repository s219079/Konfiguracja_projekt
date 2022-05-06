import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep = "\n")
product_id = input("Wprowadz identyfikator produktu: ")

opinions = pd.read_json(f"opinions/{product_id}.json")
print(opinions)