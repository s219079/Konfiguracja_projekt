import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep = "\n")
product_id = input("Wprowadz identyfikator produktu: ")

opinions = pd.read_json(f"opinions/{product_id}.json")

opinions_count = len(opinions.index)

pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
average_score = opinions.stars.mean().round(2)

recommendation = opinions.recommendation.value_counts(dropna = False)
print(recommendation)
recommendation.plot.pie(label="", autopct="%1.1", colors["forestgreen", "lightskublue", "crimson"])

plt.title("Rekomendacja")
plt.show()
plt.grid(True)
plt.close()
print(pros_count)