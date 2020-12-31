# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import page_rank_algorithm
import creating_adjaceny_from_internet
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
cmap = plt.cm.Set1.colors


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Enter a csv containing your internet: source domains should be in column 'SOURCE DOMAIN' and target "
          "domains should be in column 'TARGET DOMAIN'")
    csv_file_name = input()
    internet = pd.read_csv(csv_file_name)
    adjacency = creating_adjaceny_from_internet.makeAdjacencyList(internet)
    columns = creating_adjaceny_from_internet.makeColumnsDict(adjacency)
    matrix = creating_adjaceny_from_internet.makeAdjacencyMatrix(adjacency, columns)
    dataFrameAdjacency = pd.DataFrame(matrix, columns, columns)

    i = np.ones((matrix.shape[1], 1))
    i = i / np.linalg.norm(i, 1)
    page = page_rank_algorithm.pagerank(matrix, i)
    # I now create a dataframe of the pages and sort it by the ranking of each page
    dataFramePageRank = pd.DataFrame(page, columns, ["Page Rank"]).sort_values(by=["Page Rank"], ascending=False)
    dataFramePageRank["Ordinal Rank"] = range(len(dataFramePageRank))
    dataFramePageRank["Ordinal Rank"] = dataFramePageRank["Ordinal Rank"] + 1
    print(dataFramePageRank)
    dataFramePageRank.plot(x="Ordinal Rank", y="Page Rank", color=cmap[0])





