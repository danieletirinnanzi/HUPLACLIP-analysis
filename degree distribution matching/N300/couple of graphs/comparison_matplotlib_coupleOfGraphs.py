import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# importing averageDegreeObject.json
with open('degree distribution matching/N300/couple of graphs/currentComparisonObject_coupleOfGraphs.json') as current_comparison_file:
    current_comparison = json.load(current_comparison_file)

fig, ax = plt.subplots(figsize=(6,4))

# Extract the data that has to be plotted
x = current_comparison["arrayOfCliqueSizes"]
y_with_clique = current_comparison["graphsWithCliqueAverageDegreeArray"]
y_without_clique = current_comparison["graphsWithoutCliqueAverageDegreeArray"]
number_of_nodes = current_comparison["numberOfNodes"]
title_string = f"Average degree distribution for couple of graphs of {number_of_nodes} nodes"


# create dataframe with x, y_corrected and y_uncorrected as columns:
df = pd.DataFrame({'x': x, 'y_with_clique': y_with_clique, 'y_without_clique': y_without_clique})

# Plot the data
ax = sns.lineplot(data=df, x="x", y="y_without_clique", label="Graphs without clique (corrected)", color='blue')
ax = sns.lineplot(data=df, x="x", y="y_with_clique", label="Graphs with clique", color='red')
ax.set_ylabel("Average Degree")
ax.set_xlabel("Clique Size")
ax.legend()
ax.set_title(title_string)
fig.show()

# Save plot as high resolution png:
fig.savefig('degree distribution matching/N300/couple of graphs/images/N300_coupleOfGraphs.png', dpi=300)