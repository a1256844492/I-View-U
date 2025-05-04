from itertools import combinations
import pandas as pd

# put your primary concepts here
words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",]

# Generate all combinations and store them in a list
combinations_list = []
for i in range(2, len(words) + 1):
    for combo in combinations(words, i):
        combinations_list.append(" + ".join(combo))
    combinations_list.append("")  

# Create a DataFrame and Add the last two rows with "general investigation" and "specific investigation"
n = len(combinations_list) + 1
df = pd.DataFrame(index=range(n), columns=["concept combinations", "general investigation", "specific investigation"])

# Fill the first column
for i, combo in enumerate(combinations_list, start=1):
    df.at[i, "concept combinations"] = combo

# Remove NaN values
df.fillna("", inplace=True)

# Drop unnecessary rows
df = df.drop([0, df.index[-1]])

#save the DataFrame to a CSV file
# Make sure to change the path to your desired location
df.to_csv(r"yourpath\combinations.csv", encoding='utf-8-sig', index=False)