import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# importing averageDegreeObject.json
with open('degree distribution matching/N300/cliqueless graphs/currentComparisonObject_cliqueLessGraphs.json') as current_comparison_file:
    current_comparison = json.load(current_comparison_file)

fig, ax = plt.subplots(figsize=(6,4))

# Extract the data that has to be plotted
x = current_comparison["arrayOfCliqueSizes"]
y_uncorrected = current_comparison["uncorrectedGraphsAverageDegreeArray"]
y_corrected = current_comparison["correctedGraphsAverageDegreeArray"]
number_of_nodes = current_comparison["numberOfNodes"]
title_string = f"Average degree distribution for graphs of {number_of_nodes} nodes without clique"

# create dataframe with x, y_corrected and y_uncorrected as columns:
df = pd.DataFrame({'x': x, 'y_corrected': y_corrected, 'y_uncorrected': y_uncorrected})

# Plot the data
ax = sns.lineplot(data=df, x="x", y="y_corrected", label="Corrected graphs", color='blue')
ax = sns.lineplot(data=df, x="x", y="y_uncorrected", label="Uncorrected graphs", color = 'green')
ax.set_ylabel("Average Degree")
ax.set_xlabel("Clique Size")
ax.set_title(title_string)
ax.legend()
fig.show()

# Save plot as high resolution png:
fig.savefig('degree distribution matching/N300/cliqueless graphs/images/N300_cliqueLessGraphs.png', dpi=300)


# WITH CLIQUE (blue) - NO CLIQUE CORRECTED (red dashed) - NO CLIQUE UNCORRECTED (red filled) 